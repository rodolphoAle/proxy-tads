import threading
import requests
import os
from dotenv import load_dotenv
from app import config

load_dotenv()

class RequestCommand:
    def __init__(self, data):
        self.data = data
        self.result = None
        self.done = threading.Event()

    def execute(self):
        cpf = self.data.get("cpf")
        url = config.Config.API_URI
        headers = {"client-id": config.Config.CLIENT_ID}
        params = {"cpf": cpf}

        response = None
        try:
            if not url:
                raise ValueError("API_URI não definida")
            response = requests.get(url, headers=headers, params=params)
            content = response.json()
            self.result = {
                "response": content,
                "status_code": response.status_code
            }
        except ValueError as ve:
            content = response.text if response else str(ve)
            self.result = {
                "response": content,
                "status_code": response.status_code if response else 500
            }
        except Exception as e:
            self.result = {
                "response": {"error": str(e), "cpf": cpf},
                "status_code": 500
            }

        self.done.set()
        return self.result


