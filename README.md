# Advanced TMDB Background

These are two simple scripts to retrieve TMDB  media background and use it as Wallpaper
You must open each .py file and add your TMDB API Read Access Token
"Authorization": "Bearer XXXXX" , where XXXXX is your API
Search TMDB movie or TV shows by ID and generate background graphics Ver.1.0.0

![Movie_output](https://github.com/user-attachments/assets/5560f6bb-a6d3-454a-bed0-5d0ee9c4aca8)


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
