class SqlQueries:
    getAllTheatres = """select Id, Name, Country, City, Rating, ContactNumbers, Email from theatres;"""
    insertSlotDetails = """insert into slots(Id, StartTime, EndTime, TheatreId, MovieId, Rate) values {};"""
    makeMovieLive = """update movies set isLive = 1 where Id = {};"""
    getMovieBookingDetails = """
                        select
                        s.Id as SlotId, s.StartTime, s.EndTime, s.TheatreId, s.MovieId, s.Rate,
                        t.Name as TheatreName, t.Country, t.City, t.Rating, t.ContactNumbers, t.Email
                        from 
                        movies m inner join slots s on s.MovieId = m.Id
                        inner join theatres t on t.Id = s.TheatreId
                        where s.MovieId = {}
        """

    getSlotDetailsForId = """select * from slots where Id = {}"""
