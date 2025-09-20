from app import app
from flask import jsonify
from processor.request_queue import request_queue

@app.route("/proxy/<cpf>", methods=["GET"])
def proxy(cpf):
    # cria o comando e adiciona na fila
    cmd = request_queue.add_request({"cpf": cpf})

    # espera até o worker processar
    cmd.done.wait()

    return jsonify(cmd.result), 200
