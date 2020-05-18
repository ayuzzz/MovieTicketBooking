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
    getSlotDetailsForId = """select * from slots where Id= {};"""
    getTopBookings = """select s.Id as SlotId, m.Id as MovieId, s.StartTime, s.EndTime, m.Title, m.Imdb_score, Count(s.Id) as bookings from bookings b inner join slots s on s.Id = b.SlotId inner join movies m on m.Id = s.MovieId
                        inner join theatres t on t.Id = s.TheatreId
                        group by s.Id
                        order by Count(s.Id)
                        limit 4;   """
