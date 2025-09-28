
from flask import jsonify
from services.request_queue import get_request_queue
from routes import api_bp

@api_bp.route("/proxy/score/<cpf>", methods=["GET"])
def proxy(cpf):
    global total_requests, cache_hits, cache_misses
    total_requests += 1
    cmd = get_request_queue().add_request({"cpf": cpf})
    cmd.done.wait()
    if hasattr(cmd, "cache_hit") and cmd.cache_hit:
        cache_hits += 1
    else:
        cache_misses += 1
    return jsonify(cmd.result), 200


@api_bp.route("/metrics", methods=["GET"])
def metrics():
    metrics = get_request_queue().get_metrics()
    return jsonify(metrics), 200

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "liveness": True, "readiness": True}), 200
