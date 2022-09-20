from sqlalchemy import *
from .extensions import db

### Class Url ###


class url(db.Model):
  
    __tablename__ = 'url_shortener'


    def __init__(self):
        return

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
