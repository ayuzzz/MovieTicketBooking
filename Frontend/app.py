from flask import Flask, render_template, jsonify, request
from appsettings import Config
import requests

app = Flask(__name__)


@app.route('/')
def defaultroute():
    try:
        return "Connection to MTB app successful !!"
    except Exception as ex:
        return ex


@app.route('/home')
def homepage():
    return render_template("index.html")


@app.route('/myProfile')
def profile():
    return render_template("profile.html")


@app.route('/myTransactions')
def transactions():
    return render_template("transactions.html")


@app.route('/wishlist')
def wishlist():
    return render_template("wishlist.html")


@app.route('/movies')
def movies():
    try:
        response = requests.get(Config.getAllMoviesUrl)
        response.raise_for_status()
        return render_template("movies.html", movieList=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/movieDetails/<int:movieid>')
def movieDetails(movieid):
    try:
        response = requests.get(Config.getMovieDetailsUrl.format(movieid))
        response.raise_for_status()
        return render_template("movieDetails.html", movieDetails=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/slots')
def slots():
    try:
        response = requests.get(Config.getNonLiveMoviesUrl)
        response.raise_for_status()
        return render_template("slots.html", movieList=response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/slotDetails/<int:movieid>')
def slotDetails(movieid):
    try:
        response = requests.get(Config.getMovieDetailsUrl.format(movieid))
        response.raise_for_status()

        theatre_response = requests.get(Config.getTheatresDetailsUrl.format(movieid))
        theatre_response.raise_for_status()

        return render_template("slotDetails.html", movieList=response.json(), theatres=theatre_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


@app.route('/insertSlots', methods=['POST'])
def insertSlots():
    try:
        slotArray = request.get_json(force=True)
        response = requests.post(Config.insertSlotsUrl, json=slotArray)
        response.raise_for_status()
        result = response.json()

        movie_response = requests.get(Config.getMovieDetailsUrl.format(slotArray[0].MovieId))
        movie_response.raise_for_status()

        theatre_response = requests.get(Config.getTheatresDetailsUrl.format(slotArray[0].MovieId))
        theatre_response.raise_for_status()

        return render_template("slotDetails.html", movieList=movie_response.json(), theatres=theatre_response.json())
    except Exception as ex:
        return render_template("error.html", message=str(ex))


if __name__ == '__main__':
    app.run(debug=True)
