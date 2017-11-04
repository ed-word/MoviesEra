import requests
import json
from tmdb3 import set_key


import requests_cache
requests_cache.install_cache(cache_name='poster_cache', backend='sqlite', expire_after=86400)


def getPopular():
	key  = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)


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


	Movies = []
	for i in results:
		Movies.append(searchMovie(i['title']))

	pops = []
	for movie in Movies:
		p = movie[0].poster
		pops.append(p)

	return pops

if __name__ == "__main__":
	Movies = getPopular()
	for i in Movies[0].sizes():
		print(Movies[0].geturl(i))