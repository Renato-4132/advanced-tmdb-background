# Advanced TMDB Background

These are two simple scripts to retrieve TMDB  media background and use it as Wallpaper
You must open each .py file and add your TMDB API Read Access Token
"Authorization": "Bearer XXXXX" , where XXXXX is your API
Search TMDB movie or TV shows by ID and generate background graphics Ver.1.0.0

**How to :**
- install latest version of python (https://www.python.org/downloads/)
- Install pip (follow the process here https://pip.pypa.io/en/stable/installation/)
- Download the content of this repository
- Go into the repository using a terminal and install dependencies :
  ```
  pip install -r requirements.txt
  ```
- Edit each python scripts with your info
    - Specify you credentials
        - for Plex check this article on how to find your plex token https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
        - for TMDB create an account and get you api key here there https://www.themoviedb.org/settings/api
        - for Trakt create your account and go there https://trakt.tv/oauth/applications to create an app and retrieve your client id 
- As you run one of the script it will create a new folder and add the images automatically.
- Each time the scripts will run it will delete the content of the folder and create new images
- if you want to edit the overlay and background image I have included the source file as a vector format 

![Movie_output](https://github.com/user-attachments/assets/d12da655-d239-46e9-917d-f4f7d95f39cc)

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

# Authors:
**Renato**

**smal82** https://smal82.netsons.org/
