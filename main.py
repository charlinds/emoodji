from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import os
import webapp2

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class User(ndb.Model):
    name = ndb.StringProperty(required = True)
    username = ndb.StringProperty(required = True)
    email = ndb.StringProperty(required = True)
    password= ndb.StringProperty(required = True)
    genres = ndb.StringProperty(required = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_environment.get_template('templates/createaccount.html')

        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
            self.response.out.write('%s' % greeting)
            if

        else:
            self.response.write('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

    def post(self):
        user = users.get_current_user()
        if user:
            #if user is logged in:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                        (user.nickname(), users.create_logout_url('/')))
            existing_user = User.get_by_id(user.user_id())
            if existing_user:
                # if user is already a user, welcome 'em
                self.response.write("Welcome %s") %(existing_user.name)
            else:
                #direct new user to create-account page
                self.response.write("Welcome to our site, %s!  Please sign up! <br>")
                self.response.write(template.render())
        else:
            #if user not logged in:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
