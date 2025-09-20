import threading
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class RequestCommand:
    def __init__(self, data):
        self.data = data
        self.result = None
        self.done = threading.Event()

    def execute(self):
        cpf = self.data.get("cpf")
        url = os.getenv("API_URI")
        client_id = os.getenv("API_HEADERS")

        headers = {"client-id": client_id}
        params = {"cpf": cpf}

        try:
            response = requests.get(url, headers=headers, params=params)
            content = response.json()
        except ValueError:
            content = response.text
            self.result = {
                "response": content,
                "status_code": response.status_code                
            }
        except Exception as e:
            self.result = {
            "response": {"error": str(e), "cpf": cpf},
            "status_code": 500
        }

        # libera quem estiver esperando
        self.done.set()


