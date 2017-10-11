# this import the file media2 which has the class and webbrowser function
import media2
# this import the fresh tomatoes file which has HTML and Css for the website
import fresh_tomatoes
# this import the webbrowser function who open the website
import webbrowser
# this object form the movie class which has (movie name , trailer link , some info about the movie , photo link)
toy_story = media2.Movie("Toy Story",
                         "https://www.youtube.com/watch?v=xTZTghPGoSw",
                         "story about toys",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg")
# this object form the movie class which has (movie name , trailer link , some info about the movie , photo link)
big_hero_6 = media2.Movie("Big Hero 6", 
                          "https://www.youtube.com/watch?v=d2S8D_SCAJY", 
                          "about small boy and his repot", 
                          "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg")
# this object form the movie class which has (movie name , trailer link , some info about the movie , photo link)
assassin_creed = media2.Movie("Assassin Creed", 
                              "https://www.youtube.com/watch?v=4haJD6W136c", 
                              "about Assassin life", 
                              "https://upload.wikimedia.org/wikipedia/en/a/a0/Assassin%27s_Creed_film_poster.jpg")
# this object form the movie class which has (movie name , trailer link , some info about the movie , photo link)
forrest_gump = media2.Movie("Forrest Gump", 
                            "https://www.youtube.com/watch?v=uPIEn0M8su0", 
                            "about man life", 
                            "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg")
# this object form the movie class which has (movie name , trailer link , some info about the movie , photo link)
fight_club = media2.Movie("Fight Club", 
                          "https://www.youtube.com/watch?v=SUXWAEX2jlg", 
                          "about street fighting", 
                          "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg")
# this object form the movie class which has (movie name , trailer link , some info about the movie , photo link)
focus = media2.Movie("Foucs", 
                     "https://www.youtube.com/results?search_query=focus+trailer", 
                     "about shetting", 
                     "https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png")
# this is list contains the movies names
movies = [toy_story, big_hero_6, assassin_creed, forrest_gump, fight_club, focus]
fresh_tomatoes.open_movies_page(movies)
