import json
try:
    from .Trailer import getMovTrailer, getTVTrailer
except:
    from Trailer import getMovTrailer, getTVTrailer

class Movies:
    ID = 0
    title = ""
    poster = ""
    backdrop = ""
    trailer = ""
    overview = ""
    genreName = []
    spGenre = ""
    userrating = []
    cast = []
    director = ''


    def set(self, movie, spGenre="",castList=[]):
        self.ID = movie.id
        self.spGenre = spGenre
        try:
            self.poster = movie.poster.geturl()
        except:
            self.poster = 0
        try:
            self.backdrop = movie.backdrop.geturl()
        except:
            self.backdrop = 0
        self.overview = movie.overview
        self.title = movie.title
        try:
            self.trailer,self.cast,self.director = getMovTrailer(movie.id)
        except:
            self.trailer = 0
        x = []
        for i in movie.genres:
            x.append(i.name)
        self.genreName = x
        x = round((movie.userrating)/2)
        self.userrating = range(x)

class TV:
    ID = 0
    title = ""
    poster = ""
    backdrop = ""
    overview = ""
    genreName = []
    spGenre = ""
    isTV = "True"
    userrating = []
    cast = []

    def set(self, tv, spGenre="",castList=[]):
        self.ID = tv.id
        self.spGenre = spGenre
        try:
            self.poster = tv.poster.geturl()
        except:
            self.poster = 0
        try:
            self.backdrop = tv.backdrop.geturl()
        except:
            self.backdrop = 0
        self.overview = tv.overview
        self.title = tv.name
        x = []
        for i in tv.genres:
            x.append(i.name)
        self.genreName = x
        x = round((tv.userrating)/2)
        self.userrating = range(x)
        try:
            self.trailer,self.cast = getTVTrailer(tv.id)
        except:
            trailer = 0


genreIdDict = {10752: 'War', 80: 'Crime', 10402: 'Music', 35: 'Comedy', 36: 'History', 37: 'Western', 53: 'Thriller', 9648: 'Mystery', 12: 'Adventure', 10770: 'TV Movie', 14: 'Fantasy', 16: 'Animation', 18: 'Drama', 99: 'Documentary', 878: 'Science Fiction', 27: 'Horror', 28: 'Action', 10749: 'Romance', 10751: 'Family'}
genreNameDict = {'Romance': 10749, 'Thriller': 53, 'Mystery': 9648, 'Fantasy': 14, 'Music': 10402, 'Drama': 18, 'Horror': 27, 'Family': 10751, 'Science Fiction': 878, 'Adventure': 12, 'Documentary': 99, 'Action': 28, 'History': 36, 'Western': 37, 'TV Movie': 10770, 'War': 10752, 'Comedy': 35, 'Crime': 80, 'Animation': 16}

genreTVIdDict = {80: 'Crime', 35: 'Comedy', 37: 'Western', 10759: 'Action & Adventure', 9648: 'Mystery', 10762: 'Kids', 10763: 'News', 10764: 'Reality', 10765: 'Sci-Fi & Fantasy', 10766: 'Soap', 10767: 'Talk', 16: 'Animation', 18: 'Drama', 99: 'Documentary', 10768: 'War & Politics', 10751: 'Family'}
genreTVNameDict = {'Western': 37, 'Soap': 10766, 'Comedy': 35, 'Documentary': 99, 'Drama': 18, 'Crime': 80, 'Animation': 16, 'Family': 10751, 'Mystery': 9648, 'Action & Adventure': 10759, 'News': 10763, 'Sci-Fi & Fantasy': 10765, 'War & Politics': 10768, 'Talk': 10767, 'Reality': 10764, 'Kids': 10762}