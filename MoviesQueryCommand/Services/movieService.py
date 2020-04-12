from Repository.moviesRepository import MovieRepository


class MovieService:
    movieRepo = MovieRepository()

    def getallmovies(self):
        return self.movieRepo.getallmoviedetails()

    def getmoviedetails(self, movieid):
        return self.movieRepo.getmoviedetails(movieid)
