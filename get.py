# -*- coding:utf-8 -*-
import requests
import threading
import os
import time
from addr import *

class Monitor(threading.Thread):#Derived from the class threading.Thread
    def __init__(self, site, router, asn):
        threading.Thread.__init__(self)
        self.site = site
        self.gethtml = 'gethtml_' + site.split('.')[1] + '_' + str(asn)#get the middle part of the url
        self.router = router
        self.source_asn = asn

    def run(self):#Overwrite run() method, put what I want the thread to do here
        self.run_lg()

    def parsehtml(self, html):
        path = html
        return path

    def gethtml_as8218_8218(self):
        fexist = os.path.exists('result/' + self.gethtml.split('_')[-2] + '_' + \
                self.gethtml.split('_')[-1] + '_result')
        if fexist == True:
            os.system('rm result/' + self.gethtml.split('_')[-2] + '_' + \
                    self.gethtml.split('_')[-1] + '_result')
        for d in dest:
            print self.site
            data = {'query': 'trace', 'protocol': 'IPv6', 'addr': d,
                'router': self.router}
            r = requests.get(self.site, params = data)
            #TODO:get what we already have if time too long
            html = r.text
            path = self.parsehtml(html) 
            f = open('result/' + self.gethtml.split('_')[-2] + '_' + self.gethtml.split('_')[-1] + '_result', 'a')
            f.write(path.encode('utf8'))
            f.close()
            time.sleep(2)

    def gethtml_acad_6802(self):
        self.gethtml_as8218_8218()

    def gethtml_sunrise_6730(self):
        self.gethtml_as8218_8218()

    def gethtml_comcor_8732(self):
        self.gethtml_as8218_8218()

    #def gethtml_starttelecom(self):
    #    self.gethtml_as8218()

    def gethtml_solnet_9044(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_11260(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_23184(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_22799(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_15290(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_7018(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_553(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_6667(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_3549(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_6447(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_3303(self):
        self.gethtml_as8218_8218()

    def gethtml_eastlink_3257(self):
        self.gethtml_as8218_8218()

    def gethtml_heagmedianet_12897(self):
        self.gethtml_as8218_8218()

    def gethtml_master_24971(self):
        self.gethtml_as8218_8218()

    def gethtml_riss_34043(self):
        self.gethtml_as8218_8218()

    def gethtml_as29608_29608(self):
        self.gethtml_as8218_8218()

    def gethtml_sunnyvision_38478(self):
        self.gethtml_as8218_8218()

    def gethtml_magnet_3257(self):
        self.gethtml_as8218_8218()

    def run_lg(self):
        gethtml = getattr(self, self.gethtml)
        gethtml()

def measure():
    lg1 = Monitor('http://lg.as8218.eu', 'route-server.as8218.eu', 8218)
    lg2 = Monitor('http://netmon.acad.bg/lg', 'sf-cr-1', 6802)
    lg3 = Monitor('http://debby.sunrise.ch/lg/', 'Sunrise Routeserver', 6730)
    lg4 = Monitor('http://master.comcor.ru/lg/', 'Comcor (AS 8732)', 8732)
    #lg5 = Monitor('http://lg.starttelecom.ru', 'Moscow, Russia (M9) RA7', 8744)
    lg5 = Monitor('http://lg.solnet.ch', 'SolNet #1 (AS 9044)', 9044)
    lg6 = Monitor('http://lg.eastlink.ca', 'Eastlink Atlantic (AS 11260)', 11260)
    lg7 = Monitor('http://lg.eastlink.ca', 'Eastlink Eastern (AS 23184)', 23184)
    lg8 = Monitor('http://lg.eastlink.ca', 'Eastlink Pacific (AS 22799)', 22799)
    lg9 = Monitor('http://lg.eastlink.ca', 'Allstream (AS 15290)', 15290)
    lg10 = Monitor('http://lg.eastlink.ca', 'AT&T (AS 7018)', 7018)
    lg11 = Monitor('http://lg.eastlink.ca', 'Belwue (AS 553)', 553)
    lg12 = Monitor('http://lg.eastlink.ca', 'Eunet (AS 6667)', 6667)
    lg13 = Monitor('http://lg.eastlink.ca', 'Global Crossing (AS 3549)', 3549)
    lg14 = Monitor('http://lg.eastlink.ca', 'Oregon Exchange (AS 6447)', 6447)
    lg15 = Monitor('http://lg.eastlink.ca', 'Swisscom IP+ (AS 3303)', 3303)
    lg16 = Monitor('http://lg.eastlink.ca', 'TiNET (AS 3257)', 3257)
    lg17 = Monitor('http://lg.heagmedianet.de', 'HSE Medianet - Juniper 7003',\
            12897)
    lg18 = Monitor('http://www.master.cz/lg', 'brno-cejl-c2.masterinter.net',
            24971)
    lg19 = Monitor('http://lg.riss.ro/cgi-bin/lg.cgi', 'Core BGP-RISS-Router-01 (AS34043)', 34043)
    lg20 = Monitor('http://lg.as29608.net', 'br1.th2.par', 29608)
    lg21 = Monitor('http://lg.sunnyvision.com', ' Hong Kong - HKG', 38478)
    lg22 = Monitor('http://lg.magnet.ie', 'TISCALI (AS 3257)', 3257)
   
    lg1.start()
    lg2.start()
    lg3.start()
    lg4.start()
    #lg5.start()
    lg5.start()
    lg6.start()
    lg7.start()
    lg8.start()
    lg9.start()
    lg10.start()
    lg11.start()
    lg12.start()
    lg13.start()
    lg14.start()
    lg15.start()
    lg16.start()
    lg17.start()
    lg18.start()
    lg19.start()
    lg20.start()
    lg21.start()
    lg22.start()
    return

if __name__ == '__main__':#If I run this file alone, following codes will run.
    measure()
    
