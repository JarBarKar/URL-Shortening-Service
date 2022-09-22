from ..extensions import db
from datetime import datetime
from ..models import UrlShortener
from flask import Flask, request, jsonify, Blueprint, redirect, render_template


url_shortener_blueprint = Blueprint('url_shortener', __name__)

### Start of API point for add url ###


@url_shortener_blueprint.route("/add_url", methods=['POST'])
def add_url():
    data = request.get_json()

    try:
        originalUrl = data['url']
        if not data['url'].startswith("http://"):
            originalUrl = "http://" + data['url']

        link = UrlShortener(original_url = originalUrl)
        db.session.add(link)
        db.session.commit()
        return jsonify(
            {
                "data" : {
                    "old_url" : data['url'],
                    "new_url" : link.short_url
                },
                "message": f"{data['url']} has been successful shorten!!"
            }
        ), 200

    except Exception as e:
        return jsonify(
            {
                "error": e,
                "message": "Failure to generate new URL."
            }
        ), 500

 
### End of API points for add url ###


### Start of API point to retrieve statistics ###


@url_shortener_blueprint.route("/stats", methods=["GET"])
def get_urls_stat():
    try:
        urls = UrlShortener.query.all()
        return jsonify(
            {
                "data" : [row.to_dict() for row in urls],
                "message": f"All squashed URLs statistic have been retrieved successfully!!"
            }
        ), 200
        
    except Exception as e:
        return jsonify(
            {
                "error": e,
                "message": "Failure to retrieve URLs statistic."
            }
        ), 500
 
### End of API points to retrieve statistics ###


### Start of API point for redirect to original route ###


@url_shortener_blueprint.route("/<short_url>", methods=["GET"])
def redirect_to_original_url(short_url):
    url = UrlShortener.query.filter_by(short_url=short_url).first_or_404()
    url.visits = url.visits + 1
    db.session.commit()
    return jsonify(
        {
            "original_url" : url.original_url,
            "message":"test"
        }
    ), 200

 
### End of API points for redirect to original route ###






