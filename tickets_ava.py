from bs4 import BeautifulSoup
import requests
import sys
import emoji
import datetime
import time


# Call from command line
# Run with Python3 and use following format
# python3 tickets_ava.py MOVIE-NAME1 MOVIE-NAME2 ...

# Be sure to have dash between words in move title


def makesoup(u):
    page=requests.get(u)
    html=BeautifulSoup(page.content,"lxml")
    return html

print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
for i in range(1, len(sys.argv)):
    url = 'https://www.cineplex.com/Movie/'+sys.argv[i]
    html=makesoup(url)
    if html.find_all("div", {"class": "md-qt-widget-container no-qt"}) == [] and html.find_all("div", {"class": "md-qt-widget-container no-qt no-trailer"}) == []:
        print(sys.argv[i] + ": ✅   " + url)
    else:
        print(sys.argv[i] + ": ❌   " + url)