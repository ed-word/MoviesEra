import requests
import json
from tmdb3 import set_key
from tmdb3 import searchMovie
from tmdb3 import searchSeries
from tmdb3 import Movie
from tmdb3 import Series

try:
	from .Classes import genreIdDict, genreNameDict, genreTVIdDict, genreTVNameDict, Movies, TV
except:
	from Classes import genreIdDict, genreNameDict, genreTVIdDict, genreTVNameDict, Movies, TV


def getGenreMovieList(genresMovie):
	key = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)

	#Movie
	GenreMovieList = {}
	for genre in genresMovie:
		url = 'https://api.themoviedb.org/3/discover/movie?api_key='
		extra = '&sort_by=popularity.desc&include_adult=true&with_genres='
		url += key
		genreID = genreNameDict[genre]

		extra += str(genreID)
		url += extra

		payload = "{}"
		response = requests.request("GET", url, data=payload)

		json1_data = json.loads(response.text)
		while(1):
			try:
				results = json1_data['results']
				break
			except KeyError:
				pass		

		movie_list = []
		spare = []
		for i in results:
			if( i['genre_ids'][0]==genreID ):
				try:
					m = Movie(i['id'])
					mx = Movies()
					mx.set(movie = m, spGenre = genre)
					movie_list.append(mx)
				except:
					pass
			else:
				try:
					if( i['genre_ids'][1]==genreID ):
						try:
							m = Movie(i['id'])
							mx = Movies()
							mx.set(movie = m, spGenre = genre)
							movie_list.append(mx)
						except:
							pass
					else:
						try:
							m = Movie(i['id'])
							mx = Movies()
							mx.set(movie = m, spGenre = genre)
							spare.append(mx)
						except:
							pass
				except:
					pass

		movie_list += spare
		GenreMovieList[genre] = movie_list
	return GenreMovieList


def getGenreTVList(genresTV):
	key = '79f8797f2c2e527e4e396dfe9816a3cd'
	set_key(key)

	#TV
	GenreTVList = {}
	for genre in genresTV:
		print(genre)
		url = 'https://api.themoviedb.org/3/discover/tv?api_key='
		extra = '&sort_by=popularity.desc&with_genres='
		url += key
		
		genreID = genreTVNameDict[genre]

		extra += str(genreID)
		url += extra

		payload = "{}"
		response = requests.request("GET", url, data=payload)

		json1_data = json.loads(response.text)
		while(1):
			try:
				results = json1_data['results']
				break
			except KeyError:
				pass

		tv_list = []
		spare = []
		for i in results:
			if(i['genre_ids'][0] == genreID):
				try:
					m = Series(i['id'])
					mx = TV()
					mx.set(tv = m, spGenre=genre)
					tv_list.append(mx)
				except:
					pass
			else:
				try:
					if( i['genre_ids'][1]==genreID ):
						try:
							m = Series(i['id'])
							mx = TV()
							mx.set(tv = m, spGenre = genre)
							tv_list.append(mx)
						except:
							pass
					else:
						try:
							m = Series(i['id'])
							mx = TV()
							mx.set(tv = m, spGenre = genre)
							spare.append(mx)
						except:
							pass
				except:
					pass

		tv_list += spare
		GenreTVList[genre] = tv_list

	return GenreTVList


if __name__ == "__main__":

    genresMovie = ['Crime', 'Thriller', 'Fantasy', 'Science Fiction']
    genresTV = ['Comedy', 'Drama', 'Mystery', 'Reality']


    # genresMovie = ['Romance', 'Comedy', 'Drama']
    # genresTV = []
    GenreMovieList, GenreTVList = getGenreList(genresMovie, genresTV)

    popMovies = []
    for genre in GenreTVList:
    	print(genre)
    	print(GenreTVList[genre][0].title)
    for i in GenreMovieList['Romance']:
    	print(i.title)
