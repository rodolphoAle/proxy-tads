import requests
import time

url = 'http://127.0.0.1:5000/proxy'
headers = {'Content-Type': 'application/json'}

# Simula envio de vários CPFs
for i in range(1, 4):
    data = {
        'cpf': f'{i:011d}',
    }
    response = requests.post(url, json=data, headers=headers)
    print(f'Status: {response.status_code}, Body: {response.text}')
