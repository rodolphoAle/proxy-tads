import queue
from services.request_command import RequestCommand
from services.cache import get_cache

class RequestQueue:
    def __init__(self):
        self.queue = queue.Queue()

    def add_request(self, data):
        cpf = data.get("cpf")
        cache_key = f"score_{cpf}"
        cached_result = get_cache().get(cache_key)
        if cached_result:
            cmd = RequestCommand(data)
            cmd.result = cached_result
            cmd.done.set()
            cmd.cache_hit = True
            print("Cache hit for CPF:", cpf)
            return cmd
        
        cmd = RequestCommand(data)
        self.queue.put(cmd)
        cmd.cache_hit = False
        return cmd

    def get_request(self):
        return self.queue.get()

_request_queue_instance = None

def get_request_queue():
    global _request_queue_instance
    if _request_queue_instance is None:
        _request_queue_instance = RequestQueue()
    return _request_queue_instance