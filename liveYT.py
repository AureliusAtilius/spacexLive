import webbrowser
import json, urllib.request,codecs
def isLive(notLive, reqLen):
        
        return int(notLive)*2 < int(reqLen)


class YouTuber:

    global GOOGLE_API
    global YouTubeName
    global PlaylistID
    global data
    global videosData
    global oldVideosData
    global userID
    global liveId
    global reader
    isID = False

    def __init__(self, GOOGLE_API_KEY, User, isID = False):

        self.reader = codecs.getreader('utf-8')

        self.GOOGLE_API = GOOGLE_API_KEY
        self.YouTubeName = User
        self.isID = isID

        if not self.isID:
            self.userID = self.getUserID()

        self.PlaylistID = self.setPlaylistID()
        self.data = self.getPlaylistData()
        self.videosData = self.getVideosData(self.data)
                        
        def isUserLive(self):
                data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&type=video&eventType=live&key={}'.format(self.getUserID(), self.GOOGLE_API))))
                if len(data['items']) == 0:
                        return False
                if not len(data['items']) == 0:
                        self.liveId = self.getUserLiveData()
                        return True

        
