
import logging.config
from flask import Flask
from flask_mail import Mail
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from config import LOGGING_CONFIG


login_manager_app = LoginManager()
db = MySQL()
mail = Mail()

def create_app():
    """
    Inicializacion 
    """
    app = Flask(__name__,static_url_path="/static")
    csrf = CSRFProtect()
    csrf.init_app(app)
    app.config.from_pyfile('config/configuration.cfg')
    app.template_folder = 'templates'
    db.init_app(app)
    
    # Configurar LoginManager
    login_manager_app.init_app(app)
    login_manager_app.login_view = 'auth.login' 
    login_manager_app.login_message = 'Por favor, inicie sesión para acceder a nuestros servicios.'

    app.config['db'] = db

    # Configuraciones de Flask-Mail
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'pruebaseteagrop@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ulbu rkvo obqu jxou'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)
    logging.config.dictConfig(LOGGING_CONFIG)
    # Establecer el nivel de logs para la consola
    app.logger.setLevel(logging.DEBUG)

    # Registrar blueprints y configurar rutas...
    from .bienvenida import bienvenida
    from .carrito import carrito 
    from .ganaderia import ganaderia
    from .gatos import gatos
    from .nosotros import nosotros
    from .servicios import servicios
    from .perros import perros
    from .auth import auth
    from .error import error
    from .main import main

    app.register_blueprint(bienvenida)
    app.register_blueprint(carrito)
    app.register_blueprint(ganaderia)
    app.register_blueprint(gatos)
    app.register_blueprint(nosotros)
    app.register_blueprint(servicios)
    app.register_blueprint(perros)
    app.register_blueprint(auth)
    app.register_blueprint(error)
    app.register_blueprint(main)
    return app
