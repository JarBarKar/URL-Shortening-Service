from ..extensions import db
from datetime import datetime
from flask import Flask, request, jsonify, Blueprint


url_shortener = Blueprint('url_shortener', __name__)

### Start of API point for URL shortener ###


@url_shortener.route("/url_shortener", methods=['POST'])
def url_shortener():
    return

 
### End of API points for URL shortener ###
