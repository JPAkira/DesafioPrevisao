from dao import db,Base

class Weather(Base):
    __tablename__ = 'previsao'
    id = db.Column(db.Integer, primary_key=True)
    temp_min = db.Column(db.Float(precision=2))
    temp_max = db.Column(db.Float(precision=2))
    avg = db.Column(db.Float(precision=2))
    feels_like = db.Column(db.Float(precision=2))
    city_name = db.Column(db.String(100))
    country = db.Column(db.String(100))

    def __init__(self, temp_min, temp_max, avg, feels_like, city_name, country):
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.avg = avg
        self.feels_like = feels_like
        self.city_name = city_name
        self.country = country

    @classmethod
    def list_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_city(cls, city_name):
        return cls.query.filter_by(city_name=city_name)

    @classmethod
    def get_max(cls, max):
        return cls.query.filter_by(temp_max=max)


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {
            'temp_min': self.temp_min,
            'temp_max': self.temp_max, 
            'avg': self.avg,
            'feels_like': self.feels_like,
            'city_name': self.city_name,
            'country': self.country
        }