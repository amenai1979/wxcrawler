from urllib import request
from configparser import *
from json import load, dumps



class Wxcrawler:
    def __init__(self, configfile='default_docker.cfg'):
        self._load_config(configfile)

    def _load_config(self, configfile):
        config = ConfigParser()
        config.read(configfile)
        self._token = config['SECURITY']['TOKEN']
        self._baseurl = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['BASEPATH']

    def getWX(self, airfield='LFRO'):
        req = request.Request(self._baseurl + airfield)
        req.add_header('Authorization', self._token)
        try:
            return dumps(load(request.urlopen(req)))
        except:
            pass
if __name__== '__main__':
    crawler=Wxcrawler('default.cfg')
    print(crawler.getWX())