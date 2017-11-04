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


def getMovie(query):
	key  = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)

	#Movie
	url = 'https://api.themoviedb.org/3/search/movie?api_key='
	url += key
	url += '&query=' + query
	url += '&include_adult=true'
	payload = "{}"
	response = requests.request("GET", url, data=payload)

	json1_data = json.loads(response.text)
	while(1):
		try:
			results = json1_data['results']
			break
		except KeyError:
			pass
	
	if(len(results)==0):
		return (0,results)

	pops = []
	results = results[:3]
	for i in results:
		i = Movie(i['id'])
		mx = Movies()
		mx.set(movie=i)
		pops.append(mx)

	return (1,pops)

def getTV(query):
	key  = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)


	url = 'https://api.themoviedb.org/3/search/tv?api_key='
	url += key
	url += '&query=' + query
	payload = "{}"
	response = requests.request("GET", url, data=payload)

	json1_data = json.loads(response.text)
	while(1):
		try:
			results = json1_data['results']
			break
		except KeyError:
			pass

	if(len(results)==0):
		return (0,results)

	pops = []
	results = results[:3]
	for i in results:
		i = Series(i['id'])
		mx = TV()
		mx.set(tv=i)
		pops.append(mx)

	return (1,pops)

if __name__ == "__main__":
	flag,movies = getMovie('Big Bang')
	if(flag==0):
		print("Unsuccessful")
	else:
		for movie in movies:
			print(movie.title)