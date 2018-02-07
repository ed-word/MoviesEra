import requests
import json
from tmdb3 import set_key
from tmdb3 import searchMovie
from tmdb3 import searchSeries
from tmdb3 import Movie
from tmdb3 import Series


key  = '79f8797f2c2e527e4e396dfe9816a3cd'
youtube = 'https://www.youtube.com/watch?v='

def getMovTrailer(ID):
	
	url = 'https://api.themoviedb.org/3/movie/'
	url += str(ID) + '?api_key='
	url += key
	url += '&append_to_response=videos%2Ccredits'
	payload = "{}"
	response = requests.request("GET", url, data=payload)

	json1_data = json.loads(response.text)
	while(1):
		try:
			results = json1_data['videos']['results']
			cast = json1_data['credits']['cast']
			director = json1_data['credits']['crew'][0]['name']
			break
		except KeyError:
			pass
	trailer = youtube + results[0]['key']
	if(len(cast)>3):
		cast = cast[:3]
	cast = [i['name'] for i in cast]
	return (trailer,cast,director)

def getTVTrailer(ID):
	
	url = 'https://api.themoviedb.org/3/tv/'
	url += str(ID) + '?api_key='
	url += key
	url += '&append_to_response=videos%2Ccredits'
	payload = "{}"
	response = requests.request("GET", url, data=payload)

	json1_data = json.loads(response.text)
	while(1):
		try:
			results = json1_data['videos']['results']
			cast = json1_data['credits']['cast']
			break
		except KeyError:
			pass
	trailer = youtube + results[0]['key']
	if(len(cast)>3):
		cast = cast[:3]
	cast = [i['name'] for i in cast]
	return (trailer,cast)

if __name__ == "__main__":
	Movies,x,y = getMovTrailer(1418)
	print(Movies,x,y)