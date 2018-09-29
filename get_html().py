import requests
from bs4 import BeautifulSoup
url="https://www.yellowpages.com/search?search_terms=Coffee+Shops&geo_location_terms=7+Dublin%2C+Kingston%2C+OK"
def getHtml(url):
    
    r= requests.get(url)#Gets Html code from web
    soup = BeautifulSoup(r.content,"html.parser")#Formats html to be readable. "html.parser" is required this time for some reason
    return soup
   

print(getHtml(url))
