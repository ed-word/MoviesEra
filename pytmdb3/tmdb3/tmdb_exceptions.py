#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------
# Name: tmdb_exceptions.py    Common exceptions used in tmdbv3 API library
# Python Library
# Author: Raymond Wagner
#-----------------------


class TMDBError(Exception):
    Error = 0
    KeyError = 10
    KeyMissing = 20
    KeyInvalid = 30
    KeyRevoked = 40
    RequestError = 50
    RequestInvalid = 51
    PagingIssue = 60
    ImageSizeError = 80
    HTTPError = 90
    Offline = 100
    LocaleError = 110

    def __init__(self, msg=None, errno=0):
        self.errno = errno
        if errno == 0:
            self.errno = getattr(self, 'TMDB'+self.__class__.__name__, errno)
        self.args = (msg,)


class TMDBKeyError(TMDBError):
    pass


class TMDBKeyMissing(TMDBKeyError):
    pass


class TMDBKeyInvalid(TMDBKeyError):
    pass


class TMDBKeyRevoked(TMDBKeyInvalid):
    pass


class TMDBRequestError(TMDBError):
    pass


class TMDBRequestInvalid(TMDBRequestError):
    pass


class TMDBPagingIssue(TMDBRequestError):
    pass

class TMDBImageSizeError(TMDBError ):
    pass


class TMDBHTTPError(TMDBError):
    def __init__(self, err):
        self.httperrno = err.code
        self.response = err.fp.read()
        super(TMDBHTTPError, self).__init__(str(err))


class TMDBOffline(TMDBError):
    pass


class TMDBLocaleError(TMDBError):
    pass
