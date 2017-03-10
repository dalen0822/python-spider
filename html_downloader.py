# coding=utf-8
import urllib2

import sys


class htmlDownloader():
    def __init__(self):
        pass

    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()   # .decode(self.sysCharType).encode('utf-8')

