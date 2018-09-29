import requests
from bs4 import BeautifulSoup

url="https://www.nytimes.com/"
def getHtml(url):
    
    r= requests.get(url)#Gets Html code from web
    soup = BeautifulSoup(r.content,"html.parser")#Formats html to be readable. "html.parser" is required this time for some reason
    return soup
   
htmlData=getHtml(url)


generalData=htmlData.find_all("h2",{"class": "story-heading"})
#print(generalData[0])
#print(generalData[1].find("a"))
#print("")

#print(generalData[1].find("a").text)
#print("")

#Prints Titles
for item in generalData:
    try:
        print(item.find("a").text)
        print("")
    except:
        pass

   


        
print("")
print("")
print("")
print("")
print("")

#Prints titles + Links
"""
for item in generalData:
    try:
        print(item.find("a"))
        print("")
    except:
        pass
        """
