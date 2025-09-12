# Estrutura base para fila de requisições e processador
from processor.command import RequestCommand

class RequestQueue:
    def __init__(self):
        self.queue = []

    def add_request(self, data):
        cpf = data.get('cpf')
        if any(cmd.data.get('cpf') == cpf for cmd in self.queue):
            print(f'CPF {cpf} já está na fila. Ignorando.')
            return None
        cmd = RequestCommand(data)
        self.queue.append(cmd)
        return cmd

    def pop_request(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def process_all(self):
        """Processa todos os comandos da fila e retorna uma lista de resultados."""
        results = []
        while self.queue:
            cmd = self.pop_request()
            if cmd:
                result = cmd.execute()
                results.append(result)
        return results

request_queue = RequestQueue()