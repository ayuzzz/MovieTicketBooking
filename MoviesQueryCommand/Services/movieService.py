from Repository.moviesRepository import MovieRepository


class MovieService:
    movieRepo = MovieRepository()

    def getallmovies(self):
        return self.movieRepo.getallmoviedetails()
