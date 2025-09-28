import threading
import time
from services.request_queue import get_request_queue
from services.cache import get_cache

last_request_time = 0.0
RATE_LIMIT_SECONDS = 1.0

def worker_loop():
    global last_request_time
    while True:
        cmd = get_request_queue().get_request()

        cpf = cmd.data.get("cpf")
        cache_key = f"score_{cpf}"
        cached_result = get_cache().get(cache_key)

        if cached_result:
            cmd.result = cached_result
            cmd.done.set()
            continue
        current_time = time.time()
        time_since_last_req = current_time - last_request_time

        if time_since_last_req < RATE_LIMIT_SECONDS:
            time_to_wait = RATE_LIMIT_SECONDS - time_since_last_req
            time.sleep(time_to_wait)

        last_request_time = time.time()

        cmd.execute()

        if cmd.result and 200 <= cmd.result.get("status_code", 0) < 300:
            get_cache().put(cache_key, cmd.result)

        cmd.done.set()
        
_worker_started = False
def start_worker():
    global _worker_started
    if not _worker_started:
        t = threading.Thread(target=worker_loop, daemon=True)
        t.start()
        _worker_started = True