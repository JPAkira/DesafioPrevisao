import datetime
from schematics.models import Model
from schematics.types import StringType, DecimalType, ListType, ModelType

class WeatherReport(Model):
    temp_min = DecimalType()
    temp_max = DecimalType()
    avg = DecimalType()
    feels_like = DecimalType()
    city_name = StringType()
    country = StringType(max_length=3)

class Collection(Model):
    weathers = ListType(ModelType(WeatherReport))