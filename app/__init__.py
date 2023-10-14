from flask import Flask, jsonify, render_template, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route('/')
    def hello():
        return render_template('base.html')
    
    @app.route('/student')
    def data():
        return render_template('student.html')



    return app

























"""
from flask import Flask
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MYSQL_USER='root',
        MYSQL_PASSWORD='12345',
        MYSQL_DATABASE='mydb',
        MYSQL_HOST='localhost',
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
"""

