import yaml
import sys

import random
import string

class Config():
    def __init__(self, fileName):

        global cfg

        try:
            with open(fileName, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)
        except Exception as e:
            print(e)
            input("Press any key to exit the program")
            sys.exit()

        if not cfg['config']['connection']['Google API key']:
            input('ERROR: Missing YouTube API v3 key in config file!')
            sys.exit()


        if self.getYouTubersNr() == 0:
            input('ERROR: No YouTubers found in config file list or missing information!')
            sys.exit()

    def getConnectionData(self):
        return [cfg['config']['connection']['Google API key']]

    def getPingTime(self):
        return cfg['config']['main']['Ping Every x Minutes']

    def getYouTubersList(self):
        return cfg['config']['YouTubers']

    def getYouTubersNr(self):
        if not cfg['config']['YouTubers']:
            return 0
        return len(cfg['config']['YouTubers'])