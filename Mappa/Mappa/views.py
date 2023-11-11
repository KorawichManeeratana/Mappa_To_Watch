from flask import Blueprint, render_template, request
import json
views = Blueprint('views', __name__)

@views.route('/cinema')
def cinema():
    movie_name = request.args.get('movie')
    with open('Mappa\\Mappa\\static\\app.json') as movie:
        movie_list = json.loads(movie.read())
        for i in movie_list:
            if i['name'] == movie_name:
                return render_template("cinema.html", name=i['name'], genre=i['genre'], home=i['intro'], video_id=i['trailer'])

@views.route('/')
def home():

    return render_template("app.html")
