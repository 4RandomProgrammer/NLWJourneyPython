from flask import Flask
from src.main.routes.trip_routes import trip_routes_bp

app = Flask(__name__)

app.register_blueprint(trip_routes_bp)
