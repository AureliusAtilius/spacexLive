import requests,bs4
from requests.api import head
import liveYT


url = "https://www.youtube.com/user/spacexchannel/live"
def headLength(url):

        #create scrape to get head length
        req=requests.get(url)
        ytChannel=bs4.BeautifulSoup(req.text,'lxml')
        return len(ytChannel.head)

if __name__=="__main__":
        x=headLength(url)
        print(x)
        notLive=35
        print(liveYT.isLive(notLive,x))