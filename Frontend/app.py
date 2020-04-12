from flask import Flask, render_template, jsonify
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


@app.route('/theatres')
def theatres():
    return render_template("theatres.html")


@app.route('/payments')
def payments():
    return render_template("payments.html")


if __name__ == '__main__':
    app.run(debug=True)
