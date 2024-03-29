from flask import Flask
from flask import render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    @app.route("/")
    def display_main_page():
        return render_template("index.html")
    
    @app.route("/cars")
    def display_cars_company():
        return render_template("cars_company.html")
    

    return app
