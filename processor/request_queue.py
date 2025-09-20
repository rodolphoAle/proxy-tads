import queue
import time
from processor.request_command import RequestCommand

class RequestQueue:
    def __init__(self):
        self.queue = queue.Queue()  # fila thread-safe

    def add_request(self, data):
        cmd = RequestCommand(data)
        self.queue.put(cmd)  # coloca na fila
        return cmd

    def get_request(self):
        return self.queue.get()  # bloqueia até ter algo

# instância global
request_queue = RequestQueue()
