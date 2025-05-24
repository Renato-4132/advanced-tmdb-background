# Advanced TMDB Background

These are two simple scripts to retrieve TMDB  media background and use it as Wallpaper
You must open each .py file and add your TMDB API Read Access Token
"Authorization": "Bearer XXXXX" , where XXXXX is your API
Search TMDB movies or TV shows by ID and generate background graphics Ver.1.0.0

![Andor](https://github.com/user-attachments/assets/f146e4d6-eae6-4526-9ffd-e3d1ef3f3852)

# TMDB-cli.py

options:

  -h, --help   show this help message and exit
  
  -movie-id    The TMDB ID of the movie
  
  -tv-id       The TMDB ID of the TV show
  
  -language    Language code for TMDB metadata type (default: it)
  
  -save-path   Directory where the output will be saved type (default: tmdb_backgrounds/)
  
  -gif-gen     Generate gifs y=generate (movie_id Scan Skipped)
  
  -dura        Timing between gif imagestype (default: 5000)
  
usage: TMDB.py [-h] [-language ] [-save-path ] [-gif-gen ] [-dura ]


# TMDB.py

options:

  -h, --help   show this help message and exit
  
  -language    Language code for TMDB metadata type (default: it)
  
  -save-path   Directory where the output will be saved type (default: tmdb_backgrounds/)
  
  -gif-gen     Generate gifs y=generate
  
  -dura        Timing between gif imagestype (default: 5000)
  
usage: TMDB.py [-h] [-language ] [-save-path ] [-gif-gen ] [-dura ]
