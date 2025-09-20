# Estrutura base para fila de requisições e processador
from processor.command import RequestCommand
import threading
import time

class RequestQueue:
    def __init__(self):
        self.queue = []
        self.results = {}  # Armazena resultados por CPF

    def add_request(self, data):
        cpf = data.get('cpf')
        if any(cmd.data.get('cpf') == cpf for cmd in self.queue) or cpf in self.results:
            print(f'CPF {cpf} já está na fila ou já foi processado. Ignorando.')
            return None
        cmd = RequestCommand(data)
        self.queue.append(cmd)
        return cmd

    def pop_request(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def set_result(self, cpf, result):
        self.results[cpf] = result

    def get_result(self, cpf):
        return self.results.get(cpf)

request_queue = RequestQueue()

def worker_loop(request_queue):
    while True:
        cmd = request_queue.pop_request()
        if cmd:
            result = cmd.execute()
            cpf = cmd.data.get('cpf')
            request_queue.set_result(cpf, result)
        else:
            time.sleep(0.5)

def start_worker():
    t = threading.Thread(target=worker_loop, args=(request_queue,), daemon=True)
    t.start()

start_worker()