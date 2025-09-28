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

        try:
            response = requests.get(url, headers=headers, params=params)
            content = response.json()
            self.result = {
                "response": content,
                "status_code": response.status_code
            }
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

        self.done.set()
        return self.result


