import webbrowser
import json, urllib.request,codecs
def isLive(notLive, reqLen):
        
        return int(notLive)*2 < int(reqLen)

                
def isUserLive(GOOGLE_API,USER_ID):
        reader = codecs.getreader('utf-8')
        data = json.load(reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&type=video&eventType=live&key={}'.format(USER_ID, GOOGLE_API))))
        if len(data['items']) == 0:
                return False
        else:
                return True

        
