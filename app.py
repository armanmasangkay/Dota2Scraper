import requests
import bs4
import urllib.parse
import re
import webbrowser

res=requests.get('http://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=europe&leaderboard=1')

data=res.json()

best_player_se_asia=data['leaderboard'][0]['name']

query_string = urllib.parse.urlencode({"search_query" : best_player_se_asia +' full game'})
#html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)

#search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
website="http://www.youtube.com/results?" + query_string
#print(query_string)
webbrowser.open_new_tab(website)