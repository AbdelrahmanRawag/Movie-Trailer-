import media2
import fresh_tomatoes
import webbrowser
toy_story = media2.Movie("toy story",
                        "https://www.youtube.com/watch?v=xTZTghPGoSw",
                        "story about toys",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
                        )
#print toy_story.youtube
#toy_story.show_trailer()

big_hero_6 = media2.Movie("Big Hero 6",
                         "https://www.youtube.com/watch?v=d2S8D_SCAJY",
                         "about small boy and his repot",
                          "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg"
                         )

assassin_creed = media2.Movie("Assassin Creed",
                    "https://www.youtube.com/watch?v=4haJD6W136c",
                    "about Assassin life",
                    "https://upload.wikimedia.org/wikipedia/en/a/a0/Assassin%27s_Creed_film_poster.jpg"
                    )

forrest_gump = media2.Movie("Forrest Gump",
                          "https://www.youtube.com/watch?v=uPIEn0M8su0",
                          "about man life",
                          "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg"
                          )

fight_club = media2.Movie("Fight Club",
                           "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                           "about street fighting",
                           "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg"
                           )

focus = media2.Movie("Foucs",
                      "https://www.youtube.com/results?search_query=focus+trailer",
                      "about shetting",
                      "https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png"
                      )
movies = [toy_story,big_hero_6,assassin_creed,forrest_gump,fight_club,focus]
fresh_tomatoes.open_movies_page(movies)

