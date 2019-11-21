import requests
import bs4
import urllib.parse
import re
import webbrowser

print ('Available divisions')
print ('-------------------')
print ('A - Se_Asia\nB - Europe\nC- China\nD - Americas\n')
divDict={
   'a':'se_asia',
   'b':'europe',
   'c':'china',
   'd':'americas' 
}
val=input("Enter division:").lower()
division=divDict[val]
val2=input("Core? [y/n]:").lower()
role=0

#check if support role or not
if (val2=='y'):
    role=1
else:
    role=2

#gets the leaderboard data
res=requests.get('http://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=' +division+'&leaderboard='+str(role))

data=res.json()

best_player_se_asia=data['leaderboard'][0]['name']


#encode best player data to a url format
query_string = urllib.parse.urlencode({"search_query" : best_player_se_asia +' full game'})


#fetches the video and sorted by upload date
website="http://www.youtube.com/results?" + query_string +'&sp=CAI%253D'

webbrowser.open_new_tab(website)