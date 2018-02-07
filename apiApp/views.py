from django.shortcuts import render
from .API_ERA import popular
from .API_ERA import Classes
from .API_ERA import Genres
from .API_ERA import Search
from .API_ERA import recommend
from random import shuffle
from tmdb3 import Movie
from tmdb3 import Series
from tmdb3 import set_key
from django.contrib.auth.models import User
import pickle
from django.http import HttpResponse
import os
from django.conf import settings


key = '79f8797f2c2e527e4e396dfe9816a3cd'
set_key(key)


def slide():
    movies_tv = popular.getPopular()
    shuffle(movies_tv)

    first_movie = movies_tv[0]
    movies_tv = movies_tv[1:]

    print("\nDone with slide\n")
    return first_movie, movies_tv


def popularMovies(GenreMovieList):
    popMovies = []
    for g in GenreMovieList:
        x = GenreMovieList[g][0]
        popMovies.append(x)

    print("\nDone with popular movies\n")
    return popMovies


def popularTV(GenreTVList):
    popTV = []
    for g in GenreTVList:
        x = GenreTVList[g][0]
        popTV.append(x)

    print("\nDone with popular tv\n")
    return popTV


def refreshGenreFinal(request):
    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/tempData.p'), 'rb')
    var_dict = pickle.load(pickleFile)

    genresMovie = ['Romance', 'Comedy', 'Drama']
    GenreMovieList = Genres.getGenreMovieList(genresMovie)

    for g in GenreMovieList:
        key = g + 'Movie'
        var_dict[key] = GenreMovieList[g][0:4]
    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/data.p'), 'wb')
    pickle.dump(var_dict, pickleFile)
    return HttpResponse('<h1>GenreFinal done go to /data </h1>')


def refreshSlide(request):
    var_dict = {}
    first_movie, movies_tv = slide()
    var_dict['First'] = first_movie
    var_dict['MoviesTV'] = movies_tv

    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/tempData.p'), 'wb')
    pickle.dump(var_dict, pickleFile)
    return HttpResponse('<h1>Slide done go to /genre </h1>')


def refreshGenreMovie(request):
    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/tempData.p'), 'rb')
    var_dict = pickle.load(pickleFile)

    genresMovie = ['Crime', 'Thriller', 'Fantasy', 'Science Fiction']
    GenreMovieList = Genres.getGenreMovieList(genresMovie)

    popMovies = popularMovies(GenreMovieList)
    var_dict['popMovies'] = popMovies

    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/tempData.p'), 'wb')
    pickle.dump(var_dict, pickleFile)
    return HttpResponse('<h1>GenreMovie done go to /genreTV </h1>')


def refreshGenreTV(request):
    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/tempData.p'), 'rb')
    var_dict = pickle.load(pickleFile)

    genresTV = ['Comedy', 'Drama', 'Mystery', 'Crime']
    GenreTVList = Genres.getGenreTVList(genresTV)

    popTV = popularTV(GenreTVList)
    var_dict['popTV'] = popTV

    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/tempData.p'), 'wb')
    pickle.dump(var_dict, pickleFile)
    return HttpResponse('<h1>GenreTV done go to /genreFinal </h1>')


def refreshData(request):
    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/data.p'), 'rb')
    var_dict = pickle.load(pickleFile)
    return render(request, 'moviestar/index.html', var_dict)


def khatam(request):
    pickleFile = open(os.path.join(settings.PROJECT_ROOT, 'dataDictionary/data.p'), 'rb')
    var_dict = pickle.load(pickleFile)
    return render(request, 'moviestar/index.html', var_dict)


def movie(request, movieid):
    m = Movie(movieid)
    mx = Classes.Movies()
    mx.set(movie=m)
    mdict = {}
    mdict['movie'] = mx
    mdict['rec'] = recommend.getRecMov(movieid)
    return render(request, 'moviestar/movie.html', mdict)


def tv(request, tvid):
    t = Series(tvid)
    tx = Classes.TV()
    tx.set(tv=t)
    tdict = {}
    tdict['tv'] = tx
    tdict['rec'] = recommend.getRecTV(tvid)
    return render(request, 'moviestar/tv.html', tdict)


def search(request):
    if request.method == 'POST':
        movies_query = str(request.POST.get('movie'))
        tv_query = str(request.POST.get('tv'))

        print("Movie Query: ", movies_query)
        print("TV Query: ", tv_query)
        if movies_query:
            flag, res = Search.getMovie(movies_query)
            results = {}
            results['res'] = res
            return render(request, 'moviestar/searchMovie.html', results)
        else:
            flag, res = Search.getTV(tv_query)
            results = {}
            results['res'] = res
            return render(request, 'moviestar/searchTV.html', results)
    else:
        return render(request, 'moviestar/search.html')


def register(request):
    if request.method == 'POST':
        usermail = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(username=usermail)
        user.set_password(password)
        user.save()
        return render(request, 'rocku/login.html')
    else:
        return render(request, 'rocku/register.html')
