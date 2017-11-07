import media
import fresh_tomatoes


# instances of class Movie below
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1."
                        "jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        'G')

avatar = media.Movie('Avatar',
                     "A marine on an alien planet",
                     "http://img.goldposter.com/2015/05/Avatar_poster_goldposte"
                     "r_com_10.jpg@0o_0l_800w_80q.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     'PG-13')

fantastic_beasts = media.Movie('Fantastic Beasts and Where to Find Them',
                               "Magic in America",
                               "http://www.joblo.com/timthumb.php?src=/posters/"
                               "images/full/fantastic-beasts-poster1.jpg&h=600&"
                               "q=100",
                               "https://www.youtube.com/watch?v=Vso5o11LuGU",
                               "PG")

zootopia = media.Movie('Zootopia',
                       "Welcome to the Jungle",
                       "http://www.impawards.com/2016/posters/zootopia_xlg.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                       'PG')

arrival = media.Movie('Arrival',
                      "Aliens arrive",
                      "http://www.impawards.com/2016/posters/arrival.jpg",
                      "https://www.youtube.com/watch?v=tFMo3UJ4B4g",
                      'PG-13')

finding_dory = media.Movie('Finding Dory',
                           'Just keep swimming',
                           "http://www.impawards.com/2016/posters/finding_dory"
                           "_ver8.jpg",
                           "https://www.youtube.com/watch?v=dLIy1K8kJPo",
                           'G')

dr_strange = media.Movie('Doctor Strange',
                         'Superhero movie',
                         'http://www.joblo.com/timthumb.php?src=/posters/images/full/doctor-strange-poster.jpg&h=600&q=100',
                         'https://www.youtube.com/watch?v=Lt-U_t2pUHI',
                         'PG-13')

good_will_hunting = media.Movie('Good Will Hunting',
                                'Troubled Genius',
                                'https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg',
                                'https://www.youtube.com/watch?v=PaZVjZEFkRs',
                                'R')

goodfellas = media.Movie('Goodfellas',
                         'Life in the Mafia',
                         'https://images-na.ssl-images-amazon.com/images/I/51rOnIjLqzL.jpg',
                         'https://www.youtube.com/watch?v=qo5jJpHtI1Y',
                         'R')

movies = [toy_story, avatar, fantastic_beasts, zootopia, arrival, finding_dory,
          dr_strange, good_will_hunting, goodfellas]
fresh_tomatoes.open_movies_page(movies)
