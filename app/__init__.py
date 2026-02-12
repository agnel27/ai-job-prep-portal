from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from .routes.auth import auth_bp
    from .routes.main import main_bp
    from .routes.interview import interview_bp
    from .routes.resume import resume_bp
    from .routes.chatbox import chatbot_bp
    from .routes.analytics import analytics_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(analytics_bp)

    with app.app_context():
        db.create_all()

    return app
