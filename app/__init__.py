from flask import Flask
from dotenv import load_dotenv
from services.worker import start_worker
from services.cache import get_cache

load_dotenv()

def create_app():
    app = Flask(__name__)
    start_worker()
    get_cache()
    app.config.from_object('app.config.Config')
    app.config['APP_VERSION'] = 'v04.09.2025'
    
    from routes.routes import api_bp
    # Registra blueprints
    app.register_blueprint(api_bp)
    from routes import routes
    
    return app
