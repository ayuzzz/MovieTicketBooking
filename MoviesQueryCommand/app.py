from flask import Flask, jsonify

from Services.movieService import MovieService

app = Flask(__name__)


@app.route('/getAllMovieDetails', methods=['GET'])
def allmoviedetails():
    moviesservice = MovieService()

    return jsonify(moviesservice.getallmovies())


if __name__ == '__main__':
    app.run()
