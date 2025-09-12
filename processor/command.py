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
        client_id = self.data.get('client_id')
        if not client_id:
            print('Erro: client_id is required.')
            return
        url = os.getenv('SCORE_API_URL')
        headers = {'client-id': client_id}
        params = {'cpf': cpf}
        print(f'Processando CPF: {cpf} para client_id: {client_id}')
        try:
            response = requests.post(url, headers=headers, params=params)
            print(f'Resposta: {response.status_code} - {response.text}')
        except Exception as e:
            print(f'Erro ao requisitar: {e}')
        time.sleep(1)  # Simula processamento de 1 CPF por segundo
        print(f'Finalizado CPF: {cpf}')