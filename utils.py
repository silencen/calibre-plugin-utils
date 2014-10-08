import re,urllib2,json

def getPlayersForKeyword(keyword):
        #clean up keyword
        keyword = re.sub("(\'s|\'d|\.|,|\?|!|;|,)","",keyword)
        keyword = re.sub("(~ |~|_)"," ",keyword)
        keyword = keyword.strip()
        #grab info from REST API
        url = "http://smartsign.imtc.gatech.edu/videos?keywords=" + keyword
        response = urllib2.urlopen(url)
        #convert JSON to Python object
        info = json.load(response)
        #pull ids from converted JSON
        ids = []
        for item in info:
                ids.append(item["id"])
        #use ids to build a list of embedded players
        players = []
        for i in ids:
                players.append('<iframe width="640" height="360" align:right src="http://www.youtube.com/embed/' + i + '?rel=0"> </iframe>')
        return players