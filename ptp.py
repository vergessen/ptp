#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
import pickle

class Error(Exception):
    def __init__(self, msg):
        print(msg)

class Ptp:
    def __init__(self, username, password, passkey):
        self.session_name = 'ptp.pickle'
        self.ptpbase = 'https://passthepopcorn.me/'
        self.ptplogin = 'ajax.php?action=login'
        self.ptpsearch = 'torrents.php?searchstr=%s&json=noredirect'
        self.__login(username, password, passkey)
    def __login(self, username, password, passkey):
        self.session = self.__load()
        if not self.session or self.__expired():
            self.session = requests.Session()
            try:
                req = self.session.post(self.ptpbase + self.ptplogin, data={"username": username, "password" : password, "passkey" : passkey})
                if req.status_code == 403:
                    raise ValueError("Error")
            except ValueError as err:
                print(err)
            self.__save()
    def __expired(self):
        check = requests.get(self.ptpbase + 'torrents.php', cookies=self.session.cookies, allow_redirects=False)
        if check.status_code == 302:
            return True
        return False
    def __load(self):
        try:
            with open(self.session_name,'rb') as session_pickle:
                return pickle.load(session_pickle)
        except IOError:
            return None    
    def __save(self):
        with open(self.session_name, 'wb') as session_pickle:
            pickle.dump(self.session,session_pickle)
    def search(self, imdb):
        movie = self.session.get(self.ptpbase + self.ptpsearch % imdb).json()
        try:
            if 'Movies' in movie and int(movie['TotalResults']) > 0:
                return movie
        except:
            return None

