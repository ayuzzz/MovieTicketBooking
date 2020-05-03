from flask import Flask, jsonify

from Services.movieService import MovieService

app = Flask(__name__)


@app.route('/getAllMovieDetails', methods=['GET'])
def allmoviedetails():
    moviesservice = MovieService()

    return jsonify(moviesservice.getallmovies())


@app.route('/getNonLiveMovies', methods=['GET'])
def getNonLiveMovies():
    moviesservice = MovieService()

    return jsonify(moviesservice.getNonLiveMovies())


@app.route('/getMovieDetails/<int:movieid>', methods=['GET'])
def getMovieDetails(movieid):
    moviesservice = MovieService()

    return jsonify(moviesservice.getmoviedetails(movieid))


if __name__ == '__main__':
    app.run()
