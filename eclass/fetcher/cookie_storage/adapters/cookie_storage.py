
import os.path, os
import requests, pickle

class FileCookieStorage():
    def __init(self, path = '.'):
        self.path = path

    def restore(self, username, session):
        filename = f"{self.path}/{username}"
        if not os.path.exists(filename): return
        with open(filename, 'rb') as f:
            session.cookies.update(pickle.load(f))
    
    def store(self, username, session):
        filename = f"{self.path}/{username}"
        with open(filename, 'wb') as f:
            pickle.dump(session.cookies, f)