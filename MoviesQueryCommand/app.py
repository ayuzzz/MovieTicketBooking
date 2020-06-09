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


@app.route('/getMovieDetails/<int:movieid>/<int:userid>', methods=['GET'])
def getMovieDetails(movieid, userid):
    moviesservice = MovieService()
    return jsonify(moviesservice.getmoviedetails(movieid, userid))


@app.route('/addToWishlist/<int:movieid>/<int:userid>', methods=['POST'])
def addToWishlist(movieid, userid):
    moviesservice = MovieService()
    return jsonify(moviesservice.addToWishlist(movieid, userid))


@app.route('/wishlist/<int:userid>', methods=['GET'])
def getWishlistedMoviesForUser(userid):
    moviesservice = MovieService()
    return jsonify(moviesservice.getWishlistedMovies(userid))


@app.route('/top-movies', methods=['GET'])
def getTopMoviesList():
    moviesservice = MovieService()
    return jsonify(moviesservice.getTopMovies())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)
