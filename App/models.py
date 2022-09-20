import string
from random import choices
from sqlalchemy import *
from .extensions import db
from datetime import datetime

### Class Url ###


class UrlShortener(db.Model):
  
    __tablename__ = 'url_shortener'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String)
    short_url = db.Column(db.String)
    visits = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.convert_to_short_url()
    
    def convert_to_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url =  "".join(choices(characters, k=5))

        #Recursively call this function if generated URL exists
        if self.query.filter_by(short_url=short_url).first():
            self.convert_to_short_url

        return short_url


    def to_dict(self):
        """
        Converts the object into a dictionary,
        in which the keys correspond to database columns

        Returns
        -------
        Object of the database query
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result
### Class Url ###
