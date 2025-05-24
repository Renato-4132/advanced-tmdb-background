#!/usr/bin/env python3

import argparse
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import os
import shutil
from urllib.request import urlopen
import textwrap
from datetime import datetime, timedelta
import imageio
import sys
import subprocess

WHITE_COLOR = "\033[97m"
RED_COLOR = "\033[91m"
YELLOW_COLOR = "\033[93m"
RESET_COLOR = "\033[0m"

# ----------------- CONFIG SECTION -----------------
# Base URL for the API
url = "https://api.themoviedb.org/3/"

# Set your TMDB API Read Access Token key here
headers = {
    "accept": "application/json",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNzdhNzNlZjMzYzQyZWI4ZjdlYTQ1ODI4MzFkNDNhNyIsIm5iZiI6MTU4NTM4MDMzMy4zNTUsInN1YiI6IjVlN2VmYmVkYTQxMGM4MDAxODUyM2QxNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qWXoGG-HJU9To7RV-HpCo9uCY7uFqW-fxPGQHP4hARI"
}


custom_text_tvshow = ""
custom_text_movies = ""

parser = argparse.ArgumentParser(description="Search TMDB movies or TV shows by ID and generate background graphics Ver.1.0.0")
parser.add_argument("-movie-id", metavar='', type=int, help="The TMDB ID of the movie")
parser.add_argument("-tv-id", metavar='', type=int, help="The TMDB ID of the TV show")
parser.add_argument('-language', metavar='', type=str, default="it", help="Language code for TMDB metadata " "type (default: %(default)s)")
parser.add_argument('-save-path', metavar='', type=str, default="tmdb_backgrounds/", help="Directory where the output will be saved " "type (default: %(default)s)")
parser.add_argument("-gif-gen", metavar='', type=str,help="Generate gifs y=generate (movie_id Scan Skipped)")
parser.add_argument("-dura", metavar='', type=int,default="5000", help="Timing between gif images" "type (default: %(default)s)")

args = parser.parse_args()

movie_id = {args.movie_id}
gif_generate = {args.gif_gen}


if args.gif_gen:
   os.system('cls' if os.name == 'nt' else 'clear')
   now = datetime.now()
   print(f"{RED_COLOR}Date:{RESET_COLOR} {now.strftime('%Y-%m-%d')} {RED_COLOR}Time:{RESET_COLOR} {now.strftime('%H:%M:%S')}")
   print(f"")
   print(f"{WHITE_COLOR}-*-{RED_COLOR}Search Trending TMDB movies or TV shows and generate background gif{WHITE_COLOR}-*-{RESET_COLOR}")
   print(f"")
   output_name_gif = "Movie_output.gif"
   output_gif = args.save_path + output_name_gif
   print(f"{WHITE_COLOR}Converting files to gif..>: {RED_COLOR} {output_gif}{RESET_COLOR}")
   print(f"{WHITE_COLOR}Timing gifs..............>: {RED_COLOR} {args.dura}{RESET_COLOR}")
   image_files = sorted([os.path.join(args.save_path, file)
                     for file in os.listdir(args.save_path)
                     if file.endswith('.png') or file.endswith('.jpg')])
   with imageio.get_writer(output_gif, mode='I', duration=args.dura) as writer:
    for filename in image_files:
      image = imageio.v3.imread(filename)
      writer.append_data(image)
   print(f"{WHITE_COLOR}GIF saved as.............>: {RED_COLOR} {output_gif}{RESET_COLOR}")
   exit()

os.system('cls' if os.name == 'nt' else 'clear')
now = datetime.now()
print(f"{RED_COLOR}Date:{RESET_COLOR} {now.strftime('%Y-%m-%d')} {RED_COLOR}Time:{RESET_COLOR} {now.strftime('%H:%M:%S')}")
print(f"")
print(f"{WHITE_COLOR}-*-{RED_COLOR}Search Trending TMDB movies or TV shows and generate background gif{WHITE_COLOR}-*-{RESET_COLOR}")
print(f"")
print(f"{WHITE_COLOR}Selected movie-id......>: {RED_COLOR}{args.movie_id}{RESET_COLOR}")
print(f"{WHITE_COLOR}Selected tv-id.........>: {RED_COLOR}{args.tv_id}{RESET_COLOR}")
print(f"{WHITE_COLOR}Selected language......>: {RED_COLOR}{args.language}{RESET_COLOR}")
print(f"{WHITE_COLOR}Selected save-path.....>: {RED_COLOR}{args.save_path}{RESET_COLOR}")
print(f"{WHITE_COLOR}Selected gif-generate..>: {RED_COLOR}{args.gif_gen}{RESET_COLOR}")
print(f"")
language=args.language
savepath=args.save_path
background_dir=args.save_path

truetype_url = 'https://github.com/googlefonts/roboto/raw/main/src/hinted/Roboto-Light.ttf'
truetype_path = 'Roboto-Light.ttf'


# Download font if not present
if not os.path.exists(truetype_path):
    try:
        response = requests.get(truetype_url, timeout=10)
        if response.status_code == 200:
            with open(truetype_path, 'wb') as f:
                f.write(response.content)
            print("Roboto-Light font saved")
        else:
            print(f"Failed to download Roboto-Light font. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading the Roboto-Light font: {e}")

# Create backgrounds directory
os.makedirs(background_dir, exist_ok=True)

# ----------------- TMDB API HELPERS -----------------
def get_movie_details(movie_id):
    try:
        movie_details_url = f'{url}movie/{movie_id}?language={language}'
        resp = requests.get(movie_details_url, headers=headers)
        if resp.status_code != 200:
            print(f"Error: Movie with ID {movie_id} not found (status {resp.status_code})")
            return None
        return resp.json()
    except Exception as e:
        print(f"Error fetching movie details: {e}")
        return None

def get_tv_show_details(tv_id):
    try:
        tv_details_url = f'{url}tv/{tv_id}?language={language}'
        resp = requests.get(tv_details_url, headers=headers)
        if resp.status_code != 200:
            print(f"Error: TV show with ID {tv_id} not found (status {resp.status_code})")
            return None
        return resp.json()
    except Exception as e:
        print(f"Error fetching TV show details: {e}")
        return None

def get_logo(media_type, media_id, language={language}):
    try:
        logo_url = f"{url}{media_type}/{media_id}/images?language={language}"
        logo_response = requests.get(logo_url, headers=headers)
        if logo_response.status_code == 200:
            logos = logo_response.json().get("logos", [])
            for logo in logos:
                if logo["iso_639_1"] == "en" and logo["file_path"].endswith(".png"):
                    return logo["file_path"]
        return None
    except Exception as e:
        print(f"Error fetching logo: {e}")
        return None

def clean_filename(filename):
    return "".join(c if c.isalnum() or c in "._-" else "_" for c in filename)

def resize_image(image, height):
    ratio = height / image.height
    width = int(image.width * ratio)
    return image.resize((width, height))

def resize_logo(image, width, height):
    aspect_ratio = image.width / image.height
    new_width = width
    new_height = int(new_width / aspect_ratio)
    if new_height > height:
        new_height = height
        new_width = int(new_height * aspect_ratio)
    return image.resize((new_width, new_height))

def truncate(text, max_chars):
    if len(text) > max_chars:
        return text[:max_chars-3] + "..."
    return text

# ----------------- GRAPHICS GENERATION -----------------
def process_image(image_url, title, is_movie, genre, year, rating, duration=None, seasons=None, custom_text=""):
    # Check for required local image assets
    for asset in ["bckg.png", "overlay.png", "tmdblogo.png"]:
        if not os.path.exists(asset):
            print(f"Error: Required asset '{asset}' not found. Please ensure it is in the script directory.")
            return

    try:
        # Download the background image
        response = requests.get(image_url, timeout=10)
        if response.status_code != 200:
            print(f"Failed to download background image for {title}")
            return
        image = Image.open(BytesIO(response.content))
        image = resize_image(image, 1500)

        bckg = Image.open("bckg.png")
        overlay = Image.open("overlay.png")
        tmdblogo = Image.open("tmdblogo.0.png")

        bckg.paste(image, (1175, 0))
        bckg.paste(overlay, (1175, 0), overlay)
        bckg.paste(tmdblogo, (50, 50), tmdblogo)

        draw = ImageDraw.Draw(bckg)
        font_title = ImageFont.truetype(truetype_path, size=190)
        font_overview = ImageFont.truetype(truetype_path, size=50)
        font_custom = ImageFont.truetype(truetype_path, size=60)

        shadow_color = "black"
        main_color = "white"
        overview_color = (150, 150, 150)
        metadata_color = "white"

        title_position = (200, 420)
        overview_position = (210, 730)
        shadow_offset = 2
        info_position = (210, 650)
        custom_position = (210, 1070)

        wrapped_overview = "\n".join(textwrap.wrap(truncate(str(overview), 350), width=70, max_lines=6, placeholder=" ..."))

        draw.text((overview_position[0] + shadow_offset, overview_position[1] + shadow_offset), wrapped_overview, font=font_overview, fill=shadow_color)
        draw.text(overview_position, wrapped_overview, font=font_overview, fill=metadata_color)

        if is_movie:
            genre_text = genre
            additional_info = f"{duration}"
        else:
            genre_text = genre
            additional_info = f"{seasons} {'Season' if seasons == 1 else 'Seasons'}"

        rating_text = "TMDB: " + str(rating)
        year_text = truncate(str(year), 7)
        info_text = f"{genre_text}  \u2022  {year_text}  \u2022  {additional_info}  \u2022  {rating_text}"

        draw.text((info_position[0] + shadow_offset, info_position[1] + shadow_offset), info_text, font=font_overview, fill=shadow_color)
        draw.text(info_position, info_text, font=font_overview, fill=overview_color)

        logo_path = get_logo("movie" if is_movie else "tv", movie_id if is_movie else tv_id, language="en")
        logo_drawn = False

        if logo_path:
            logo_url = f"https://image.tmdb.org/t/p/original{logo_path}"
            logo_response = requests.get(logo_url)
            if logo_response.status_code == 200:
                try:
                    logo_image = Image.open(BytesIO(logo_response.content))
                    logo_image = resize_logo(logo_image, 1000, 500)
                    logo_position = (210, info_position[1] - logo_image.height - 25)
                    logo_image = logo_image.convert('RGBA')
                    bckg.paste(logo_image, logo_position, logo_image)
                    logo_drawn = True
                except Exception as e:
                    print(f"Failed to draw logo for {title}: {e}")

        if not logo_drawn:
            draw.text((title_position[0] + shadow_offset, title_position[1] + shadow_offset), title, font=font_title, fill=shadow_color)
            draw.text(title_position, title, font=font_title, fill=main_color)

        if custom_text:
            draw.text((custom_position[0] + shadow_offset, custom_position[1] + shadow_offset), custom_text, font=font_custom, fill=shadow_color)
            draw.text(custom_position, custom_text, font=font_custom, fill=metadata_color)

        filename = os.path.join(background_dir, f"{clean_filename(title)}.jpg")
        bckg = bckg.convert('RGB')
        bckg.save(filename)
        print(f"{WHITE_COLOR}Image saved: {RED_COLOR}{filename}{RESET_COLOR}")
        print(f" ")
    except Exception as e:
        print(f"Error processing image for {title}: {e}")

# ----------------- COMMAND LINE INTERFACE -----------------
def cli_search_by_id():

    if args.movie_id:
        movie = get_movie_details(args.movie_id)
        if not movie:
            print("Movie not found!")
            return
        title = movie.get("title", "Unknown Title")
        global overview
        overview = movie.get("overview", "")
        if not overview:
         print(f"{YELLOW_COLOR}No {args.language} plot found for {title}{RESET_COLOR}")
         print(f"{YELLOW_COLOR}https://www.themoviedb.org/movie/{args.movie_id}/edit{RESET_COLOR}")
         overview = "We do not have a translated description. Help us expand our database by adding one."
        year = (movie.get("release_date") or "")[:4]
        rating = round(movie.get("vote_average", 0), 1)
        genre = ', '.join([g["name"] for g in movie.get("genres", [])]) if "genres" in movie else ""
        duration = movie.get("runtime", 0)
        if duration:
            hours = duration // 60
            minutes = duration % 60
            duration_str = f"{hours}h{minutes}min"
        else:
            duration_str = "N/A"
        backdrop_path = movie.get("backdrop_path")
        #Extra custom text below plot
        custom_text=custom_text_movies
        if backdrop_path:
            image_url = f"https://image.tmdb.org/t/p/original{backdrop_path}"
            global movie_id, tv_id
            movie_id, tv_id = args.movie_id, None
            process_image(
                image_url, title, is_movie=True, genre=genre, year=year,
                rating=rating, duration=duration_str, custom_text=custom_text
            )
        else:
            print("No backdrop image found for this movie.")
    elif args.tv_id:
        tv = get_tv_show_details(args.tv_id)
        if not tv:
            print("TV show not found!")
            return
        title = tv.get("name", "Unknown Title")
        overview = tv.get("overview", "")
        if not overview:
          print(f"{YELLOW_COLOR}No {args.language} plot found for {title}{RESET_COLOR}")
          print(f"{YELLOW_COLOR}https://www.themoviedb.org/tv/{args.tv_id}/edit{RESET_COLOR}")
          overview = "We do not have a translated description. Help us expand our database by adding one."
        year = (tv.get("first_air_date") or "")[:4]
        rating = round(tv.get("vote_average", 0), 1)
        genre = ', '.join([g["name"] for g in tv.get("genres", [])]) if "genres" in tv else ""
        seasons = tv.get("number_of_seasons", 0)
        backdrop_path = tv.get("backdrop_path")
        #Extra custom text below plot
        custom_text = custom_text_tvshow
        if backdrop_path:
            image_url = f"https://image.tmdb.org/t/p/original{backdrop_path}" 
            movie_id, tv_id = None, args.tv_id           
            process_image(
                image_url, title, is_movie=False, genre=genre, year=year,
                rating=rating, seasons=seasons, custom_text=custom_text
            )
        else:
            print("No backdrop image found for this TV show.")
    else:
        parser.print_help()
        print()


if __name__ == "__main__":
    cli_search_by_id()
