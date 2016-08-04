from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import os
import webapp2
import models
from random import *

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

#TEST MAINPAGE
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
            template = jinja_environment.get_template('templates/signin.html')
            self.response.write(template.render())

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

        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))

        self.response.write('Thanks for signing up, %s! <br> %s' % (emoodji_user.first_name, signout_link_html))

        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
<<<<<<< Updated upstream

class SettingsHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            # users shouldn't be able to get here without being logged in
            self.error(500)
            return
        emoodji_user = models.EmoodjiUser.get_by_id(user.user_id())

        existing_user = {'existing_username': emoodji_user.username,
                        'exisiting_first':emoodji_user.first_name,
                        'existing_last': emoodji_user.last_name
                        }


        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))

        self.response.write('Click to sign out, %s! <br> %s' % (emoodji_user.first_name, signout_link_html))
        self.response.write("Hey, "+ emoodji_user.first_name + " use the space below to update your information :)")
        template = jinja_environment.get_template('templates/createaccount.html')
        self.response.write(template.render(existing_user))

=======

class SettingsHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            # users shouldn't be able to get here without being logged in
            self.error(500)
            return


        self.response.write("Welcome to our site, please create an account")
        template = jinja_environment.get_template('templates/createaccount.html')
        self.response.write(template.render({'existing_username': ,}))


        emoodji_user = models.EmoodjiUser(
            first_name= self.request.get('first_name'),
            last_name = self.request.get('last_name'),
            username= self.request.get('username'),
            #WHAT TO DO FOR GENRES (ARRAY)??
            genres= self.request.get('song', allow_multiple = True),
            id= user.user_id()
            )
        emoodji_user.put()

        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))

        self.response.write('Thanks for signing up, %s! <br> %s' % (emoodji_user.first_name, signout_link_html))

        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
>>>>>>> Stashed changes

# FUNCTIONALITY of emoojis page (mainpage) HANDLER
#the functionality of actually getting the songs
#remember: user and emoodji user are set to have the same id

class FunctionHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        emoodji_account = models.EmoodjiUser.get_by_id(user.user_id())
        print emoodji_account
        if not emoodji_account:
            self.redirect('/')
        songs = []
        song_query = models.Song.query().fetch()

        for song in song_query:
            #print song
            print song.genre
            #print song.mood
            #print self.request.get("mood")
            print emoodji_account.genres
            if song.genre in emoodji_account.genres and song.mood == self.request.get("mood"):
                songs.append(song.link)
            #     # print "working!!!"
            # else:
            #     print "BLECKHHHH :("

        shuffle(songs)

        songs = songs[0:3]
        #print songs
        template_values= {'links': songs, 'mood': self.request.get("mood")}
        #get first three elements
        #put in dictionary (template_values) [to pass to template later
        #pass to template

        signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
        self.response.write('Thanks for signing up, %s! <br> %s' % (emoodji_account.first_name, signout_link_html))

        template = jinja_environment.get_template('templates/playlist.html')
        self.response.write(template.render(template_values))

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


#NEED A IF STATEMNET FOR INTERNATIONAL??
            #if usermood == international
            #     template = jinja_environment.get_template('templates/      .html')
            #     self.response.write(template.render())
            #
        # print song_query
        # print emoodji_account.genres


        # song_data = song_query.filter(Song.genres in user_genres)
        # mood = happy
        #
        # for song in song_data:
        #     if song.mood == mood:
        #         songs.append(song)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/emoodji', EmojiHandler),
    ('/playlist', FunctionHandler),
    ('/setting', SettingsHandler)
], debug=True)
