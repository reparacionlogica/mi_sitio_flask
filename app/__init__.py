from flask import Flask

def create_app():
    app = Flask(__name__)
    # si luego usas sesiones/flash: app.config["SECRET_KEY"] = "cambia-esto"

    # registrar rutas desde routes.py (blueprint)
    from .routes import bp
    app.register_blueprint(bp)

    return app



