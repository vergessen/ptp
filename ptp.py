#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests

class Ptp:
    def __init__(self, apiuser,apikey):
        self.session_name = 'ptp.pickle'
        self.ptpbase = 'https://passthepopcorn.me/'
        self.ptpsearch = 'torrents.php?searchstr=%s'
        self.headers = {"ApiUser": apiuser, "ApiKey" : apikey}
        self.apiuser = apiuser
        self.apikey = apikey
        req = requests.get(self.ptpbase + 'index.php', headers=self.headers)
    def search(self, imdb):
        movie = requests.get(self.ptpbase + self.ptpsearch % imdb, headers=self.headers).json()
        try:
            if 'Movies' in movie and int(movie['TotalResults']) > 0:
                return movie
        except:
            return None

