# Estrutura base para fila de requisições e processador
from processor.command import RequestCommand

class RequestQueue:
    def __init__(self):
        self.queue = []

    def add_request(self, data):
        cpf = data.get('cpf')
        client_id = data.get('client_id')
        if not client_id:
            print('Erro: client_id é obrigatório.')
            return False
        if any(cmd.data.get('cpf') == cpf for cmd in self.queue):
            print(f'CPF {cpf} já está na fila. Ignorando.')
            return False
        cmd = RequestCommand(data)
        self.queue.append(cmd)
        return True

    def pop_request(self):
        if self.queue:
            return self.queue.pop(0)
        return None

request_queue = RequestQueue()