from app import create_app
from dotenv import load_dotenv
import sys

load_dotenv()

app = create_app()

if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    app.run(debug=True)