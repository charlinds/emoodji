from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import os
import webapp2
import models
from random import *

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class EmojiHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            #if user is logged in as a google user:
            #matching the user id in emoodji to the one in google
            emoodji_user = models.EmoodjiUser.get_by_id(user.user_id())
            #link to sign out (thanks google)
            signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
            #if user is emoodji user as well, welcome 'em
            if emoodji_user:
                self.response.write("Welcome %s %s! <br> %s" % (emoodji_user.first_name, emoodji_user.last_name, signout_link_html))
                template = jinja_environment.get_template('templates/mainpage.html')
                self.response.write(template.render())
            #if user is not an emoodji user: createaccount page
            else:
                self.response.write("Welcome to our site, please create an account")
                template = jinja_environment.get_template('templates/createaccount.html')
                self.response.write(template.render())
        else:
            self.response.write('Please log in to use our site! <br> <a href="%s">Sign in</a>' % (users.create_login_url('/')))

    def post(self):
        user = users.get_current_user()
        if not user:
            # users shouldn't be able to get here without being logged in
            self.error(500)
            return

        emoodji_user = models.EmoodjiUser(
            first_name= self.request.get('first_name'),
            last_name = self.request.get('last_name'),
            username= self.request.get('username'),
            #WHAT TO DO FOR GENRES (ARRAY)??
            genres= self.request.get('song', allow_multiple = True),
            id= user.user_id()
            )
        emoodji_user.put()
        self.response.write('Thanks for signing up, %s!' % emoodji_user.first_name)


# FUNCTIONALITY of emoojis page (mainpage) HANDLER
#the functionality of actually getting the songs
#remember: user and emoodji user are set to have the same id

class FunctionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        emoodji_account = models.EmoodjiUser.get_by_id(user.user_id())
        if not emoodji_account:
            self.redirect('/')
        # genre = self.request.get('genre')
        # user_genres = emoodji_account.genres
        # if genre in user_genres and mood == mood
        # songs = []

    # TEST - DO NOT ERASE
        # self.response.write('<h1> Your Genre is: ' + emoodji_account.genres[0] + '</h1>')
        # song_query = models.Song.query().fetch()
        # for song in song_query:
        #     if song.genre in emoodji_account.genres:
        #         self.response.write('<p>' + song.artist + ' has song:' + song.title + '</p>')
    # END OF TEST

    #TEST for "mood" from mainpage
        #self.response.write('<h1> Your Genre is: ' + self.request.get("mood") + '</h1>')
    #END OF TEST

        songs = []
        song_query = models.Song.query().fetch()

            #if usermood == international
            #     template = jinja_environment.get_template('templates/      .html')
            #     self.response.write(template.render())
            #
        for song in song_query:
            if song.genre in emoodji_account.genres and song.mood == self.request.get("mood"):
                songs.append(song)

    ####WHAT TO RETURN:
        # return a specific number of songs
        # random.randint(0, len(songs))
        # if(   )
        # link = song.link -->then DISPLAY

        # song_data = song_query.filter(Song.genres in user_genres)
        # mood = happy
        #
        # for song in song_data:
        #     if song.mood == mood:
        #         songs.append(song)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/emoodji', EmojiHandler),
    ('/testing', FunctionHandler)
], debug=True)
