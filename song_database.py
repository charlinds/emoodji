from google.appengine.ext import ndb
import webapp2


class Song(ndb.Model):
    title = ndb.StringProperty(required = True)
    genre = ndb.StringProperty(required = True)
    mood = ndb.StringProperty(required = True)
    link = ndb.StringProperty(required = True)
    artist = ndb.StringProperty(required = True)

songs = [
#ALTERNATIVE
    Song(title = "Fix You",
        genre= "Alternative",
        mood= "sad",
        link = "k4V3Mo61fJM",
        artist = "Coldplay"
        ),
    Song(title = "Bad Religion",
         genre= "Alternative",
         mood= "sad",
         link = "eTOzANfO15g",
         artist = "Frank Ocean"
         ),
    Song(title = "Fine For Now",
         genre= "Alternative",
         mood= "sad",
         link = "75nPmkegHyU",
         artist = "Grizzly Bear"
         ),
    Song(title= "Holy Smoke",
         genre= "Alternative",
         mood= "sleepy",
         link = "BNHwMgKCXZ8",
         artist = "Vashti Bunyan"
         ),
    Song(title= "Between the Bars",
         genre= "Alternative",
         mood= "sleepy",
         link = "hPD-a1FjUtU",
         artist = "Elliot Smith"
         ),
    Song(title= "Diane Young",
         genre= "Alternative",
         mood= "party",
         link = "oG6lTQNW04I",
         artist = "Vampire Weekend"
         ),
    Song(title= "Mr.Brightside",
         genre= "Alternative",
         mood= "party",
         link ="gGdGFtwCNBE",
         artist="The Killers"
         ),
    Song(title= "The Middle",
         genre= "Alternative",
         mood= "happy",
         link= "oKsxPW6i3pM",
         artist= "Jimmy Eat World"
         ),
    Song(title= "every Other Freckle",
         genre= "Alternative",
         mood= "happy",
         link ="-mhgfXgwdls",
         artist="Alt J"
         ),

#CLASSICAL
    Song(title= "O Lead Me To Some Peaceful Gloom",
         genre= "Classical",
         mood= "sad",
         link ="gXCubgc1ZvA",
         artist="Henry Purcell"
         ),
    Song(title= "Prelude in E-minor",
         genre= "Classical",
         mood= "sad",
         link ="ef-4Bv5Ng0w",
         artist="Frederic Chopin"
         ),
    Song(title= "Concerto for Two Cellos in G minor Largo",
         genre= "Classical",
         mood= "sad",
         link ="tST-v7LUuTE",
         artist="Vivaldi"
         ),
    Song(title= "Cantata 140",
         genre= "Classical",
         mood= "sleepy",
         link ="JCULWK4tNuc",
         artist="J.S. Bach"
         ),
    Song(title= "Mozart Piano Concerto No. 21 Andante",
         genre= "Classical",
         mood= "sleepy",
         link ="df-eLzao63I",
         artist="Mozart"
         ),
    Song(title= "Clair de Lune",
         genre= "Classical",
         mood= "sleepy",
         link ="vG-vmVrHOGE",
         artist="Claude Debussy"
         ),
    Song(title= "Piano Quartet in C minor op 15 -Scherzo",
         genre= "Classical",
         mood= "happy",
         link ="0VLm3xMocRY",
         artist="Brahms"
         ),
    Song(title= "Schubert Piano Trio No 2 (3rd mvt)",
         genre= "Classical",
         mood= "happy",
         link ="CRz6iezcvL8",
         artist="Schubert"
         ),
    Song(title= "Moonlight Sonata 2nd Mvt",
         genre= "Classical",
         mood= "happy",
         link ="h1z9RRQ8t9k",
         artist="Beethoven"
         ),
    Song(title= "Toccata and Fugue in D Minor",
         genre= "Classical",
         mood= "angry",
         link ="ho9rZjlsyYY",
         artist="J.S. Bach"
         ),
    Song(title= "Moonlight Sonata 3rd Mvt.",
         genre= "Classical",
         mood= "angry",
         link ="nW95YnFrvPc",
         artist="Beethoven(Arthur Rubinstein)"
         ),
    Song(title= "Mozart Requiem Dies Irae",
         genre= "Classical",
         mood= "angry",
         link ="RKJur8wpfYM",
         artist="Mozart"
         ),
    Song(title= "Vivaldi The Four Seasons: Spring",
         genre= "Classical",
         mood= "party",
         link ="aFHPRi0ZeXE",
         artist="Vivaldi"
         ),
    Song(title= "Cello Suite No.1 in G ",
         genre= "Classical",
         mood= "party",
         link = "mGQLXRTl3Z0",
         artist= "Bach"
         ),
    Song(title= "Hungarian Rhapsody no 6 in Db Major ",
         genre= "Classical",
         mood= "party",
         link ="Z3V2g5kqdM4",
         artist= "Liszt"
         ),
#HIP-HOP/R&B
    Song(title="Real Friends",
        genre = "Hip-Hop/R&B",
        mood = "party",
        link = "Q4flyJgyyHk",
        artist = "Kanye West"
            ),
    Song(title="Can't Tell Me Nothing",
        genre = "Hip-Hop/R&B",
        mood = "party",
        link = "E58qLXBfLrs",
        artist = "Kanye West"
        ),
    Song(title="Lite Weight",
        genre = "Hip-Hop/R&B",
        mood = "party",
        link = "wifV7bj6dYk",
        artist = "Anderson.Paak"
        ),
    Song(title="Homecoming",
        genre = "Hip-Hop/R&B",
        mood = "party",
        link = "LQ488QrqGE4",
        artist = "Kanye West"
        ),
    Song(title="Ghetto Walkin'",
        genre = "Hip-Hop/R&B",
        mood = "sad",
        link = "A9U8y4aWveE",
        artist = "Miles Davis, Robert Glasper, Bilal"
        ),
    Song(title="When Will U Call",
        genre = "Hip-Hop/R&B",
        mood = "sad",
        link = "A9U8y4aWveE",
        artist = "Bilal"
        ),
    Song(title="Why Do We Try",
        genre = "Hip-Hop/R&B",
        mood = "sad",
        link = "zASay0KjZ3A",
        artist = "Robert Glasper"
        ),
    Song(title="Mobius Streak",
        genre = "Hip-Hop/R&B",
        mood = "sleepy",
        link = "lCvMtQSdCXo",
        artist = "Hiatus Kaiyote"
        ),
    Song(title="Bird of Space",
        genre = "Hip-Hop/R&B",
        mood = "sleepy",
        link = "_xTrNLXAAK8",
        artist = "Jose James"
        ),
    Song(title="Twice",
        genre = "Hip-Hop/R&B",
        mood = "sleepy",
        link = "flk-zI90rDw",
        artist = "Robert Glasper"
        ),

#POP
    Song(title="Happy",
        genre = "Pop",
        mood = "happy",
        link = "y6Sxv-sUYtM",
        artist = "Pharrell"
        ),
    Song(title="How to Be a Heartbreaker",
        genre = "Pop",
        mood = "happy",
        link = "vKNcuTWzTVw",
        artist = "Marina and the Diamonds"
        ),
    Song(title="Stacy's Mom",
        genre = "Pop",
        mood = "party",
        link = "ykPlT2G_HeM",
        artist = "Bowling for Soup"
        ),
    Song(title="Sorry",
        genre = "Pop",
        mood = "party",
        link = "8ELbX5CMomE",
        artist = "Justin Bieber"
        ),
    Song(title="Fix a Heart",
        genre = "Pop",
        mood = "sad",
        link = "_vIqho2Es4k",
        artist = "Demi Lovato"
        ),
    Song(title="Remembering Sunday",
        genre = "Pop",
        mood = "sad",
        link = "ccKV1X9uyP4",
        artist = "All Time Low"
        ),

#ROCK
    Song(title="In a Broken Dream",
        genre = "Rock",
        mood = "angry",
        link = "PV5oDDelJrM",
        artist = "Rod Stewart"
        ),
    Song(title="My War",
        genre = "Rock",
        mood = "angry",
        link = "8eMvryXDHWQ",
        artist = "Black Flag"
        ),
    Song(title="I Miss You",
        genre = "Rock",
        mood = "sad",
        link = "s1tAYmMjLdY",
        artist = "Blink-182"
        ),
    Song(title="Vienna",
        genre = "Rock",
        mood = "sad",
        link = "oZdiXvDU4P0",
        artist = "Billy Joel"
        ),
    Song(title="If",
        genre = "Rock",
        mood = "sad",
        link = "e2G8EWy-plM",
        artist = "Pink Floyd"
        ),
    Song(title="Your Song",
        genre = "Rock",
        mood = "sleepy",
        link = "13GD78Bmo8s",
        artist = "Elton John"
        ),
    Song(title="Iron Sky",
        genre = "Rock",
        mood = "sleepy",
        link = "ELKbtFljucQ",
        artist = "Paolo Nutini"
        ),
    Song(title="Ramble On",
        genre = "Rock",
        mood = "party",
        link = "a3HemKGDavw",
        artist = "Led Zeppelin"
        ),
    Song(title="Dancing in the Moonlight",
        genre = "Rock",
        mood = "party",
        link = "0yBnIUX0QAE",
        artist = "Toploader"
        ),

#INTERNATIONAL
    Song(title="Je vais vite",
        genre = "International",
        mood = "French",
        link = "SvpZMjcjo_g",
        artist = "Lorie"
        ),
    Song(title="Quelqu'un m'a dit",
        genre = "International",
        mood = "French",
        link = "EC7Re8cczj0",
        artist = "Carla Bruni"
        ),
    Song(title="Maria Maria",
        genre = "International",
        mood = "Spanish",
        link = "593bk4N5im0",
        artist = "Claudia Acuna"
        ),
    Song(title="Kun Anta",
        genre = "International",
        mood = "Arabic",
        link = "qKVW_wJs91Q ",
        artist = "Humood"
        ),
    Song(title="Duele el corazon",
        genre = "International",
        mood = "Spanish",
        link = "FutjZEBTXs ",
        artist = "Enrique Iglesias"
        ),
    Song(title="Papaoutai",
        genre = "International",
        mood = "French",
        link = "oiKj0Z_Xnjc ",
        artist = "Stromae"
        ),
    Song(title="Mehbooba Mehbooba",
        genre = "International",
        mood = "Indian",
        link = "aZ7lf5rtzoI",
        artist = "Rahul Dev Burman"
        ),
    Song(title="Wa ollak eh",
        genre = "International",
        mood = "Arabic",
        link = "fS7Hv43EkZw",
        artist = "Hamza Namira"
        ),

#JAZZ
    Song(title= "West of the West",
        genre= "Jazz",
        mood= "angry",
        link= "H8FLvHFUbTY",
        artist= "Christian Scott"),
    Song(title="Free Jazz",
        genre="Jazz",
        mood= "angry",
        link="xbZIiom9rDA",
        artist="Ornette Coleman"),
    Song(title="Mr. Clean",
        genre="Jazz",
        mood= "angry",
        link="k5CNYsmAJwI",
        artist="Freddie Hubbard"),
    Song(title="I Want To Feel Good Pt. 2",
        genre="Jazz",
        mood= "happy",
        link="t9QisECfWKI",
        artist="The Bad Plus"),
    Song(title="Joy Spring",
        genre="Jazz",
        mood= "Happy",
        link="dnK6OHPQZbA",
        artist="Clifford Brown"),
    Song(title="Look At The Birdie",
        genre="Jazz",
        mood= "sleepy",
        link="DKMqNKx9n8M",
        artist="Art Blakey"),
    Song(title="Moon Dreams",
        genre="Jazz",
        mood= "sleepy",
        link="iDjeXUxbvGI",
        artist="Miles Davis"),
    Song(title="All Blues",
        genre="Jazz",
        mood= "sleepy",
        link="JIfdYs8WErM",
        artist="Miles Davis"),
    Song(title="Speak Low",
        genre="Jazz",
        mood= "sleepy",
        link="S7Qgms3pgqE",
        artist="Roy Hargrove (Kurt Weill, Ogden Nash)"),
    Song(title="Neptune (The Planet)",
        genre="Jazz",
        mood= "sad",
        link="DzD5aEc_zPI",
        artist="The Bad Plus"),
    Song(title="Bird Of Paradise",
        genre="Jazz",
        mood= "sad",
        link="dqhb6tRTLNo",
        artist="Charile Parker"),
    Song(title="Body And Soul",
        genre="Jazz",
        mood= "sad",
        link="zUFg6HvljDE",
        artist="Coleman Hawkins (Gertrude Lawrence)"),
    Song(title="Nellie Bly",
        genre="Jazz",
        mood= "party",
        link="IZl12wxfghU",
        artist="David Weiss"),
    Song(title="Art of War",
        genre="Jazz",
        mood= "party",
        link="KX9nWp0WBhw",
        artist="Orrin Evans"),
    Song(title="Festival",
        genre="Jazz",
        mood= "party",
        link="bjS76L7Gvnw",
        artist="Robert Glasper")
]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        ndb.put_multi(songs)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
