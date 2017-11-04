import requests
import json
from tmdb3 import set_key
from tmdb3 import searchMovie
from tmdb3 import searchSeries
from tmdb3 import Movie
from tmdb3 import Series

try:
	from .Classes import Movies, TV
except:
	from Classes import Movies, TV

import requests_cache
requests_cache.install_cache(cache_name='popular_cache', backend='sqlite', expire_after=86400)

def getRecMov(ID):
	key  = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)

	#Movie
	url = 'https://api.themoviedb.org/3/movie/'
	url += str(ID) + '/recommendations?api_key='
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
	results = results[0:2]

	pops = []
	for i in results:
		m = Movie(i['id'])
		mx = Movies()
		mx.set(movie=m)
		pops.append(mx)

	return pops

def getRecTV(ID):
	#TV
	key  = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)

	url = 'https://api.themoviedb.org/3/tv/'
	url += str(ID) + '/recommendations?api_key='
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
	results = results[0:2]

	pops = []
	for i in results:
		m = Series(i['id'])
		mx = TV()
		mx.set(tv = m)
		pops.append(mx)

	return pops


if __name__ == "__main__":
	Movies = getRecTV(1418)
	for movie in Movies:
		print(movie.title)