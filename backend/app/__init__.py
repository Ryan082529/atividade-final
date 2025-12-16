from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .config import Config


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()

def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "error": "Validation Error",
            "messages": error.messages
        }), 400

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return jsonify({
            "error": error.name,
            "message": error.description
        }), error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        return jsonify({
            "error": "Internal Server Error",
            "message": str(error)
        }), 500

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY'] = 'chave-secreta-supersegura'  # Troque em produção!
    app.json.sort_keys = False
    app.url_map.strict_slashes = False

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(
    app,
    supports_credentials=True,
    resources={
        r"/*": {
            "origins": [
                "https://verbose-potato-jv4794r747jfpjrg-5173.app.github.dev"
            ]
        }
    },
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
) 
    @jwt.unauthorized_loader
    def unauthorized_response(err_str):
        return jsonify({ "error": "Token JWT ausente ou inválido", "message": err_str }), 401

    @jwt.invalid_token_loader
    def invalid_token_response(err_str):
        return jsonify({"error": "Token inválido", "message": err_str }), 422

    from .routes.messages import messages_bp
    app.register_blueprint(messages_bp, url_prefix="/mensagens")

    with app.app_context():
        from .models.user import User
        from .models.message import Message
        from .models.comment import Comment
        db.create_all()


    from app.routes.comments import comments_bp
    app.register_blueprint(comments_bp)

    from app.routes.users import users_bp
    app.register_blueprint(users_bp)
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    register_error_handlers(app)

    return app
