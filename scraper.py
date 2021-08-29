import requests,bs4



url = "https://www.youtube.com/user/spacexchannel/live"
def headLength(url):

        #create scrape to get head length
        req=requests.get(url)
        ytChannel=bs4.BeautifulSoup(req.text)
        return len(ytChannel.head)

