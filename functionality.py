# the functionality of actually getting the songs
#user and emoodji user are set to have the same id

from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

user = users.get_current_user()
emoodji_account = EmoodjiUser.get_by_id(user.user_id)

user_genres = emoodji_account.genres

songs = []

song_query = Song.query()

# song_data = song_query.filter(Song.genres == user_genres)

mood = happy

for song in song_data:
    if song.mood == mood:
        songs.append(song)
