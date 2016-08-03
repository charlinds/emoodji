from google.appengine.ext import ndb

class EmoodjiUser(ndb.Model):
    first_name = ndb.StringProperty(required = True)
    last_name = ndb.StringProperty(required = True)
    username = ndb.StringProperty(required = True)
    #DON'T need email because it's already stored in google
        #email = ndb.StringProperty(required = True)
    # NEVER STORE PASSWORD because you can get HACKED
        #password = ndb.StringProperty(required = True)
    genres = ndb.StringProperty(repeated= True)
    #repeated used for arrays


class Song(ndb.Model):
    title = ndb.StringProperty(required = True)
    genre = ndb.StringProperty(required = True)
    mood = ndb.StringProperty(required = True)
    link = ndb.StringProperty(required = True)
    artist = ndb.StringProperty(required = True)
