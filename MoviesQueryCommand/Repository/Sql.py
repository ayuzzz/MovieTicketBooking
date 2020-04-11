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
                    from movies limit 20
                   """