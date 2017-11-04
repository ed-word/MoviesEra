import requests
import json
from tmdb3 import set_key
from tmdb3 import searchMovie
from tmdb3 import searchSeries
from tmdb3 import Movie
from tmdb3 import Series

try:
	from .Classes import genreIdDict, genreNameDict, genreTVIdDict, genreTVNameDict
except:
	from Classes import genreIdDict, genreNameDict, genreTVIdDict, genreTVNameDict

key  = '79f8797f2c2e527e4e396dfe9816a3cd'
set_key(key)

#Movie
url = 'https://api.themoviedb.org/3/movie/popular?api_key='
url += key
payload = "{}"
response = requests.request("GET", url, data=payload)

json1_data = json.loads(response.text)
while(1):
	try:
		results = json1_data['results']
		break
	except KeyError:
		pass
results = results[0]['id']

results = Movie(results)

results = results.id
print(results)
for i in results:
	print(i)