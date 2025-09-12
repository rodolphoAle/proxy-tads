from app import app
from flask import request, jsonify
from processor.base_processor import request_queue

@app.route('/proxy', methods=['POST'])
def proxy():
    # Recebe requisição do cliente e adiciona à fila
    data = request.get_json()
    print(f'Received data: {data}')
    request_queue.add_request(data)
    return jsonify({'status': 'Request received and queued.'}), 202