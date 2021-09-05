import webbrowser,time, liveYT, scraper



def main():

        baseLength=35
        #url="https://www.youtube.com/user/spacexchannel/live"
        url ="https://www.youtube.com/c/NASASpaceflightVideos/live"
        
        while True:
                # Check if channel is live by checking header length
                if not liveYT.isLive(baseLength,scraper.headLength(url)):
                        baseLength=scraper.headLength(url)
                        # Check every 60 seconds
                        time.sleep(60)
                        continue
                else:
                        #Get current time
                        timeOfDay=time.localtime(time.time())
                        hour=timeOfDay.tm_hour
                        # Check time to not open stream before 8AM or after 9PM
                        if hour>=8 and hour<=21:
                                # Open livestream
                                webbrowser.open(url)
                        # Wait an hour before checking again.
                        time.sleep(3600)
                        continue

if __name__=="__main__":
        main()
        