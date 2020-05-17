from Repository.moviesRepository import MovieRepository


class MovieService:
    movieRepo = MovieRepository()

    def getallmovies(self):
        return self.movieRepo.getallmoviedetails()

    def getNonLiveMovies(self):
        return self.movieRepo.getNonLiveMovies()

    def getmoviedetails(self, movieid, userid):
        return self.movieRepo.getmoviedetails(movieid, userid)

    def addToWishlist(self, movieid, userid):
        return self.movieRepo.addToWishlist(movieid, userid)

    def getWishlistedMovies(self, userid):
        return self.movieRepo.getWishlistedMovies(userid)
