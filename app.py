from app import create_app
from dotenv import load_dotenv
import sys

load_dotenv()

app = create_app()
if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
