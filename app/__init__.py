from flask import Flask, render_template
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from config import CLOUD_NAME,API_KEY,API_SECRET 
from flask_wtf.csrf import CSRFProtect
import cloudinary
import cloudinary.uploader
import cloudinary.api

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
     )

    cloudinary.config( 
      CLOUD_NAME=CLOUD_NAME, 
      API_KEY=API_KEY, 
      API_SECRET=API_SECRET 
    )
    
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    from .functions import students_bp as students_blueprint
    app.register_blueprint(students_blueprint)

    from .functions import courses_bp as courses_blueprint
    app.register_blueprint(courses_blueprint)

    from .functions import colleges_bp as colleges_blueprint
    app.register_blueprint(colleges_blueprint)

    return app