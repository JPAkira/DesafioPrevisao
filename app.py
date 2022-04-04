# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from Previsao.resources.weather_resource import WeatherResource, MaxWeatherResource, WeatherPostResource
from dao import db
from cache import cache

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = '8d8f469ed2ef36f537797449f494f738ff6e498cfa63e3761df5196dbc0a36ad'

api = Api(app)
CORS(app,resources={r"/*": {"origins": "*"}}) 

@app.before_first_request
def create_tables():
    print("Create Tables")
    db.create_all()

api.add_resource(WeatherPostResource, '/post/')
api.add_resource(WeatherResource, '/temperature/<string:city_name>')
api.add_resource(MaxWeatherResource, '/temperature')


if __name__ == '__main__':
    db.init_app(app)
    cache.init_app(app)
    app.run(port=5000,debug=True)