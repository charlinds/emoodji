from google.appengine.ext import ndb

class Song(ndb.Model):
    title = ndb.StringProperty(required = True)
    genre = ndb.StringProperty(required = True)
    mood = ndb.StringProperty(required = True)
    link = ndb.StringProperty(required = True)
