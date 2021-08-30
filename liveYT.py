import webbrowser

def isLive(notLive, reqLen):
        
        return int(notLive)*2 < int(reqLen)

                

def openStream(url):
                webbrowser.open(url)
        
