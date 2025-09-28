from flask import jsonify
from services.request_queue import get_request_queue
from routes import api_bp

@api_bp.route("/proxy/score/<cpf>", methods=["GET"])
def proxy(cpf):    
    cmd = get_request_queue().add_request({"cpf": cpf})
    cmd.done.wait()

    return jsonify(cmd.result), 200
