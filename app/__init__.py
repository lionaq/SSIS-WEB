from flask import Flask, render_template
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, CLOUD_NAME, API_KEY, API_SECRET
from flask_wtf.csrf import CSRFProtect
import cloudinary

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
    )
          
    cloudinary.config( 
        cloud_name = CLOUD_NAME, 
        api_key = API_KEY, 
        api_secret = API_SECRET,
        secure=True,
    )


    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)
    
    # a simple page that says hello
    @app.route('/')
    def default():

        return render_template('base.html')
    
    from .controller.student_controller import student
    from .controller.course_controller import course
    from .controller.college_controller import college

    app.register_blueprint(student)
    app.register_blueprint(course)
    app.register_blueprint(college)
    
    return app

