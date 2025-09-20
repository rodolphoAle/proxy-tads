# Command Pattern: encapsula requisições
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class RequestCommand:
    def __init__(self, data):
        self.data = data

    def execute(self):
        cpf = self.data.get('cpf')
        url = os.getenv('SCORE_API_URL')
        client_id = os.getenv('SCORE_API_HEADERS')
        headers = {'client-id': client_id}
        params = {'cpf': cpf}
        print(f'Processando CPF: {cpf} para client_id: {client_id}')
        try:
            response = requests.post(url, headers=headers, params=params)
            print(f'Resposta: {response.status_code} - {response.text}')
            result = {
                'cpf': cpf,
                'status_code': response.status_code,
                'response': response.json() if response.headers.get('Content-Type', '').startswith('application/json') else response.text
            }
        except Exception as e:
            print(f'Erro ao requisitar: {e}')
            result = {
                'cpf': cpf,
                'error': str(e)
            }
        time.sleep(2)  # Simula processamento de 2 CPF por segundo
        print(f'Finalizado CPF: {cpf}')
        return result