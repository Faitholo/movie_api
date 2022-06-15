from distutils.debug import DEBUG
import json
from flask import Flask, render_template, url_for, jsonify
import requests
import os

import urllib.request, json

from dotenv import load_dotenv
load_dotenv('/home/faith/movie_api/.env')


app = Flask(__name__)

@app.route('/')
def hello():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("API_KEY1"))
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template ("movies.html", movies=dict["results"])

@app.route("/movies")
def get_movies_list():
    url = "https://api.themoviedb.org/3/discover/movie?api_key={}".format(os.environ.get("API_KEY1"))

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)

    return {"results": movies}


@app.route('/dictionary')
def get_word():
    app_id  = os.environ.get('ID')
    app_key  = os.environ.get('API_KEY2')
    endpoint = "entries"
    language_code = "en-us"
    word_id = "example"
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    
    d_text = r.text
    j_form = json.dumps(r.json())
    
    #print("code {}\n".format(r.status_code))
    #print("text \n" + r.text)
    #print("json \n" + json.dumps(r.json()))
    
    return jsonify({
        'status': True,
        'text': d_text,
        'data': j_form
        })


if __name__ == '__main__':
    app.run(debug=True)
