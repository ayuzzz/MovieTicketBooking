class SqlQueries:
    getAllMovies = """
                    select
                    Id,
                    Title,
                    Duration,
                    Genres,
                    Plot_keywords,
                    Director_name,
                    Language,
                    Country,
                    Content_rating,
                    Budget,
                    Release_year,
                    Movie_imdb_link,
                    Imdb_score,
                    Movie_fblikes,
                    Director_fblikes,
                    Actor1_name,
                    Actor1_fblikes,
                    Actor2_name,
                    Actor2_fblikes,
                    Actor3_name,
                    Actor3_fblikes
                    from movies where isLive = 1
                   """

    getMovieDetails = """
                        select
                        m.Id,
                        Title,
                        Duration,
                        Genres,
                        Plot_keywords,
                        Director_name,
                        Language,
                        Country,
                        Content_rating,
                        Budget,
                        Release_year,
                        Movie_imdb_link,
                        Imdb_score,
                        Movie_fblikes,
                        Director_fblikes,
                        Actor1_name,
                        Actor1_fblikes,
                        Actor2_name,
                        Actor2_fblikes,
                        Actor3_name,
                        Actor3_fblikes,
                        IF (w.Id is null, 'N', 'Y') as inWishlist
                        from movies m left join wishlist w on w.MovieId = m.Id and w.UserId = {1}
                        where m.Id = {0}
                       """

    getNonLiveMovies = """
                    select
                    Id,
                    Title,
                    Duration,
                    Genres,
                    Plot_keywords,
                    Director_name,
                    Language,
                    Country,
                    Content_rating,
                    Budget,
                    Release_year,
                    Movie_imdb_link,
                    Imdb_score,
                    Movie_fblikes,
                    Director_fblikes,
                    Actor1_name,
                    Actor1_fblikes,
                    Actor2_name,
                    Actor2_fblikes,
                    Actor3_name,
                    Actor3_fblikes
                    from movies where isLive = 0
                   """

    addToWishlist = """insert into wishlist values (0, {1}, {0});"""

    getWishlist = """select m.* from movies m inner join wishlist w on w.MovieId = m.Id and w.UserId = {};"""

    getTopMovies = """select m.* from bookings b inner join slots s on s.Id = b.SlotId inner join movies m on m.Id = s.MovieId
                      inner join theatres t on t.Id = s.TheatreId
                      group by m.Id
                      order by Count(s.Id)
                      limit 3; """