import threading
import time
from processor.request_queue import request_queue

def worker_loop():
    while True:
        cmd = request_queue.get_request()  # espera até ter algo
        result = cmd.execute()

        # coloca o resultado no próprio comando
        cmd.result = result
        cmd.done.set()   # sinaliza que terminou
        time.sleep(1)

def start_worker():
    t = threading.Thread(target=worker_loop, daemon=True)
    t.start()
