import requests,bs4
from requests.api import head



url = "https://www.youtube.com/user/spacexchannel/live"
def headLength(url):

        #create scrape to get head length
        req=requests.get(url)
        ytChannel=bs4.BeautifulSoup(req.text,'lxml')
        return len(ytChannel.head)

print(headLength(url))