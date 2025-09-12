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
        clientId = self.data.get('clientId')
        if not clientId:
            print('Erro: clientId is required.')
            return
        url = os.getenv('SCORE_API_URL')        
        headers = os.getenv('SCORE_API_HEADERS')
        params = {'cpf': cpf}
        print(f'Processando CPF: {cpf}')
        try:
            response = requests.post(url, headers=headers, params=params)
            print(f'Resposta: {response.status_code} - {response.text}')
        except Exception as e:
            print(f'Erro ao requisitar: {e}')
        time.sleep(1)  # Simula processamento de 1 CPF por segundo
        print(f'Finalizado CPF: {cpf}')