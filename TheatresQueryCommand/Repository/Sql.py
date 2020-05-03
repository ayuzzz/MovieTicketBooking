class SqlQueries:
    getAllTheatres = """select Id, Name, Country, City, Rating, ContactNumbers, Email from theatres;"""
    insertSlotDetails = """insert into slots(Id, StartTime, EndTime, TheatreId, MovieId, Rate) values {};"""
    makeMovieLive = """update movies set isLive = 1 where Id = {};"""
