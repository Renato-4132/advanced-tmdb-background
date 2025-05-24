# Advanced TMDB Background

These are two simple scripts to retrieve TMDB  media background and use it as Wallpaper

Search TMDB movies or TV shows by ID and generate background graphics Ver.1.0.0
TMDB-cli.py
options:
  -h, --help   show this help message and exit
  -movie-id    The TMDB ID of the movie
  -tv-id       The TMDB ID of the TV show
  -language    Language code for TMDB metadata type (default: it-IT)
  -save-path   Directory where the output will be saved type (default: tmdb_backgrounds/)
  -gif-gen     Generate gifs y=generate (movie_id Scan Skipped)
  -dura        Timing between gif imagestype (default: 5000)
usage: TMDB.py [-h] [-language ] [-save-path ] [-gif-gen ] [-dura ]


TMDB.py
options:
  -h, --help   show this help message and exit
  -language    Language code for TMDB metadata type (default: it)
  -save-path   Directory where the output will be saved type (default: tmdb_backgrounds/)
  -gif-gen     Generate gifs y=generate
  -dura        Timing between gif imagestype (default: 5000)
usage: TMDB.py [-h] [-language ] [-save-path ] [-gif-gen ] [-dura ]
