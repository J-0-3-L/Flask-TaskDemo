from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import Config

db= SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from app.routes.task import bp as task


        app.register_blueprint(task)

        db.create_all()
    return app