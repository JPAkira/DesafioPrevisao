from flask_restful import Resource, reqparse, abort
from Previsao.schemas.weather import Collection, WeatherReport
from Previsao.models.main import Weather
from config import DEFAULT_MAX_NUMBER
from flask import request
from cache import cache


class WeatherResource(Resource):
    def get(self, city_name):
        json_return = ''
        try:
            query = Weather.find_by_city(city_name)
            if query:
                itens = {'weathers': list(map(lambda x: x.json(), query))}
                schema = Collection(itens)
                json_return = schema.to_primitive()
                cities = cache.get("cities")
                if not cities:
                    cities = {}
                if not city_name in cities.keys():
                    cities[city_name] = json_return
                    cache.set("cities", cities)
            else:
                abort(404, message="Not Found")
        except Exception as e:
            print(e)
            abort(404, message="Not Found")

        return json_return,201

class MaxWeatherResource(Resource):
    def get(self): 
        json_return = ''
        max = request.args['max'] or DEFAULT_MAX_NUMBER
        cities = cache.get("cities")
        if not cities:
            abort(404, message="Not Found")
        try:
            max = int(max)
            if len(cities.keys()) < max:
                max = len(cities.keys())
            json_return = {k: cities[k] for k in list(cities)[:max]}
        except Exception as e:
            print(e)
            abort(404, message="Not Found")

        return json_return,201


class WeatherPostResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('temp_min', type=float)
    parser.add_argument('temp_max', type=float)
    parser.add_argument('avg', type=float)
    parser.add_argument('feels_like', type=float)
    parser.add_argument('city_name', type=str)
    parser.add_argument('country', type=str)

    def post(self):
        json = ''
        try:
            raw_data = WeatherPostResource.parser.parse_args()
            item = WeatherReport(raw_data)
            item.validate()
            data = item.to_primitive()
            weather = Weather(**data)
            weather.save_to_db()
            json = weather.json()

        except Exception as e:
            print(e)
            abort(500, message="An error occurred inserting the item.")
        return json, 201