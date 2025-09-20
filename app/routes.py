from app import app
from flask import request, jsonify
from processor.base_processor import request_queue
import time

@app.route('/proxy', methods=['POST'])
def proxy():
    # Recebe requisição do cliente e adiciona à fila
    data = request.get_json()
    print(f'Received data: {data}')
    cmd = request_queue.add_request(data)
    if not cmd:
        return jsonify({'message': 'CPF já está na fila ou já foi processado.'}), 200

    # Aguarda o processamento do CPF e retorna o resultado
    cpf = data.get('cpf')
    timeout = 30  # segundos
    waited = 0
    while waited < timeout:
        result = request_queue.get_result(cpf)
        if result is not None:
            return jsonify(result), 200
        time.sleep(0.2)
        waited += 0.2
    return jsonify({'message': 'Timeout ao processar o CPF.'}), 504