from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # from .main import main as main_blueprint #blue print are added to make a map of of whole project / to structure the project
    # app.register_blueprint(main_blueprint)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)


    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db = SQLAlchemy(app)
    db.init_app(app)


    # class User(db.Model):
    #     id=db.Column(db.Integer, primary_key=True)
    #     email=db.Column(db.String(100) , unique=True)
    #     name=db.Column(db.String(100))
    #     password=db.Column(db.String(100))

    with app.app_context():
        db.create_all()
    
    from .main import main as main_blueprint #blue print are added to make a map of of whole project / to structure the project
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app

    # with app.app_context():
    #     db.create_all()

    # app.run(debug=True)

 

# to run the app : flask --app flask_project_exercise run --debug

# create_app()