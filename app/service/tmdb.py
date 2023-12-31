import tmdbsimple as tmdb
import pandas as pd

tmdb.API_KEY = '77b3e44f983ea9bfc6eae8182d00e4c9'

def getActorId(name):
    id = -1
    try:
        search = tmdb.Search()
        search_results = search.person(query=name)
        id = search.results[0]['id']
    except Exception as e:
        print(repr(e))
    return id

def getMovieCredits(actorId):
    person = tmdb.People(actorId)
    return person.movie_credits()['cast']

def toDataframe(movieCredits):
    movie_credits_df = pd.DataFrame(movieCredits)
    return movie_credits_df.loc[:,('title','id','release_date', 'popularity','vote_average')].sort_values('release_date')

def getData(actor):
    actorId = getActorId(actor)
    if (actorId == -1):
        print('Actor could not be found')
        return pd.DataFrame()
    credits = getMovieCredits(actorId)
    return toDataframe(credits)