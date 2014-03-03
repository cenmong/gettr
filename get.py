# -*- coding:utf-8 -*-
import requests
import threading
import os
from addr import *

class Monitor(threading.Thread):#Derived from the class threading.Thread
    def __init__(self, site, router):
        threading.Thread.__init__(self)
        self.site = site
        self.parser = 'parse_' + site.split('.')[-2]#get the middle part of the url
        self.router = router

    def run(self):#Overwrite run() method, put what I want the thread to do here
        self.run_lg()

    def parse_as8218(self):
        fexist = os.path.exists(self.parser.split('_')[-1] + '_result')
        if fexist == True:
            os.system('rm ' + self.parser.split('_')[-1] + '_result')
        for d in dest:
            print '*************************************************************'
            data = {'query': 'trace', 'protocol': 'IPv6', 'addr': d,
                'router': self.router}
            r = requests.get(self.site, params = data)
            html = r.text
            f = open(self.parser.split('_')[-1] + '_result', 'a')
            f.write(html)
            f.close()

    def parse_acad(self):
        self.parse_as8218()

    def run_lg(self):
        parser = getattr(self, self.parser)
        parser()

def measure():
    lg1 = Monitor('http://lg.as8218.eu', 'route-server.as8218.eu')
    lg2 = Monitor('http://netmon.acad.bg/lg', 'sf-cr-1')
    lg1.start()
    lg2.start()
    return

if __name__ == '__main__':#If I run this file alone, following codes will run.
    measure()
    
