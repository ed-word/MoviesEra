from django.shortcuts import render
from .API_ERA import popular
from .API_ERA import Classes
from .API_ERA import Genres
from .API_ERA import Search
from .API_ERA import recommend
from random import shuffle
from django.views.decorators.cache import cache_page
from tmdb3 import Movie
from tmdb3 import Series
from tmdb3 import set_key

key = '79f8797f2c2e527e4e396dfe9816a3cd'
set_key(key)


def slide():
    movies_tv = popular.getPopular()
    shuffle(movies_tv)

    first_movie = movies_tv[0]
    movies_tv = movies_tv[1:]

    return first_movie, movies_tv


def popularMovies(GenreMovieList):
    popMovies = []
    for g in GenreMovieList:
        x = GenreMovieList[g][0]
        popMovies.append(x)

    return popMovies


def popularTV(GenreTVList):
    popTV = []
    for g in GenreTVList:
        x = GenreTVList[g][0]
        popTV.append(x)

    return popTV


def gen_vardict():
    var_dict = {}
    first_movie, movies_tv = slide()
    var_dict['First'] = first_movie
    print(len(first_movie.genreName), "\t", first_movie.title)
    for c in movies_tv:
        print(len(c.genreName), "\t", c.title)
    var_dict['MoviesTV'] = movies_tv

    genresMovie = ['Crime', 'Thriller', 'Fantasy', 'Science Fiction']
    genresTV = ['Comedy', 'Drama', 'Mystery', 'Reality']
    GenreMovieList, GenreTVList = Genres.getGenreList(genresMovie, genresTV)
    popMovies = popularMovies(GenreMovieList)
    popTV = popularTV(GenreTVList)
    var_dict['popMovies'] = popMovies
    var_dict['popTV'] = popTV

    genresMovie = ['Romance', 'Comedy', 'Drama']
    genresTV = []
    GenreMovieList, _ = Genres.getGenreList(genresMovie, genresTV)

    for g in GenreMovieList:
        key = g + 'Movie'
        var_dict[key] = GenreMovieList[g][0:4]
    return var_dict


@cache_page(60 * 1440)
def khatam(request):
    var_dict = gen_vardict()
    # cache.set('var_dict',var_dict,60*1440)
    # var_dict = cache.get('var_dict')
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


'''
# def registration(request,p):
    # if request.method=='POST':
    #     print (p)
    #     fname = request.POST.get('fname')
    #     lname = request.POST.get('lname')

    #     profile_pic = request.FILES['profile_pic']

    #     day = request.POST.get('day')
    #     month = request.POST.get('month')
    #     year = request.POST.get('year')

    #     gender = request.POST.get('gender')

    #     city = request.POST.get('city')
    #     country = request.POST.get('country')

    #     upass = request.POST.get('upass')
    #     upass1 = request.POST.get('upass1')

    #     print (fname)
    #     print(lname)
    #     print(day)
    #     print(month)
    #     print(year)
    #     print(gender)
    #     print(city)
    #     print(country)

    #     if upass == upass1:
    #         up = User.objects.get(password=p)
    #         print (up)

    #         userprofile = UserProfile.objects.create(user=up,first_name=fname
    ,last_name=lname,
    #             profile_pic=profile_pic,day=day,month=month,year=year,gender=gender,
    #             city=city,country=country)
    #         userprofile.save()
    #         up.set_password(upass)
    #         up.save()

    #         user = authenticate(username=up.username, password=upass)

    #         if user.is_active:
    #             auth_login(request, user)

    #             return redirect('/profile/')


    #         else:
    #             return HttpResponse("Unexpected Error! Please Try Again.")

    #     else:
    #         return HttpResponse('Enter password correctly')

    # else:
    #     up=User.objects.get(password=p)
    #     print (up)
    #     return render(request,'pages/details.html',{ 'p':p, 'day':range(31),
    #     'year':range(1980,2017) })




def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/')

            else:
                context['error'] = 'Non active user'
        else:
            context['error'] = 'Wrong username or password'
    else:
        context['error'] = ''

    # populateContext(request, context)

    return render(request, 'rocku/login.html', context)



def logout(request):
    context = {}
    if request.user.is_authenticated():
        auth_logout(request)
        # context['error'] = 'Some error occured.'

    #   populateContext(request, context)
    return render(request, 'rocku/login.html', context)



# def populateContext(request, context):
#     context['authenticated'] = request.user.is_authenticated()
#     if context['authenticated'] == True:
#         context['username'] = request.user.username
        # auth_logout(request)

# Create your views here.

    # def friend_list(request):
    #     context = {}
    #     fb_uid = SocialAccount.objects.filter(user_id=request.user.id,
    provider='facebook')
    #     print ('hi')
    #     print (fb_uid[0].uid)
    #     if fb_uid.exists():
    #         fb_uid = fb_uid[0].uid
    #         tolken = SocialToken.objects.filter(account__user=request.user,
    account__provider='facebook').first()
    #         #tolken='EAACEdEose0cBAPnFKDHpJpq7wvScCDma9dxd1V17NEejvVy2U0rVVbkOiX5aXHOjhapHyFaG5Ayo5dyAFCI0Ufv6aZA9wD0uNRRbxE0IOM4fRDWrWidJsGUuRNHm0RuIDEv5lhij5wKJZBJEOaEJKj7b6i5HlOdOhJPzLnA6TaP6H8CzK5gOWeLneoM6YZD'
    #         print(tolken)
    #         returned_json = requests.get("https://graph.facebook.com/v2.10/"
    + fb_uid + "/friends?access_token="
    + 'EAACEdEose0cBAPnFKDHpJpq7wvScCDma9dxd1V17NEejvVy2U0rVVbkOiX5'
    'aXHOjhapHyFa'
    'G5Ayo5dyAFCI0Ufv6aZA9wD0uNRRbxE0IOM4fRDWrWidJsGUuRNHm0RuIDEv5lhij5wKJZBJEOaEJKj7b6i5HlOdOhJPzLnA6TaP6H8CzK5gOWeLneoM6YZD')
    #         targets = returned_json.json()['data']
    #         print(targets)
    #         # id_list = [target['id'] for target in targets]
    #         # friends = SocialAccount.objects.filter(uid__in=id_list)
    #         # print(friends)
    #         # context['friends'] = friends
    #     return render(request,'friendslist.html',)

def friend_list(request):
    context = {}
    fb_uid = SocialAccount.objects.filter(user_id=request.user.id,
    provider='facebook')
    print ('hi')
    print (fb_uid[0].uid)
    if fb_uid.exists():
        fb_uid = fb_uid[0].uid
        tolken = SocialToken.objects.filter(account__user=request.user,
        account__provider='facebook').first()
        # returned_json = requests.get("https://graph.facebook.com/v2.9/"
        + fb_uid
        + "/friends?access_token=" + str(tolken))
        print(tolken)
        returned_json = requests.get("https://graph.facebook.com/v2.10/"
        + fb_uid
        + "?fields=friends{name}&access_token=" + str(tolken))
        #   print(returned_json.json()['friends'])
        # targets = returned_json.json()['data']
        # id_list = [target['id'] for target in targets]
        # friends = SocialAccount.objects.filter(uid__in=id_list)
        # context['friends'] = friends
        print (context)
    return render(request,'friendslist.html',{'friends':context})


def fblogin(request):
    return render(request,'fblogin.html')


def register(request):
    if(request.method=='POST'):
        some_var=request.POST.getlist('checks[]')
        print (len(some_var))
        print (some_var)
        return HttpResponse('fuck you')
    else:
        genrelist=genre.objects.all()
        print(genrelist)
        return render(request,'register.html',{'genrelist':genrelist})


def temp(request):
    return render(request,'moviestar/temp.html')



def dashboard(request):
    # u = customUser()
    u.setAttr(obj=request)
    return render(request,'moviestar/single-movie.html')
'''
