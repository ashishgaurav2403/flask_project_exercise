from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .main import main as main_blueprint #blue print are added to make a map of of whole project / to structure the project
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app