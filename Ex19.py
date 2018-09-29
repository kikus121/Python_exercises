import requests
from bs4 import BeautifulSoup

def getHtml(url):
    
    r= requests.get(url)#Gets Html code from web
    soup = BeautifulSoup(r.content,"html.parser")#Formats html to be readable. "html.parser" is required this time for some reason
    return soup
   
"""
for i in range(1,5):
    print("")
    print("")
    print("Page {}".format(i))
    print("")
    print("")
    url="http://gramynamaxa.pl/publicystyka_index.php?page={}".format(i)
    htmlData=getHtml(url)
    generalData=htmlData.find_all("div",{"class": "content"})
    for item in generalData:
         try:
            print(item.find("a").text)
      
            print("")
      
         except:
              pass
"""              
url="https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
htmlData=getHtml(url)
generalData=htmlData.find_all("section",{"class": "content-section"})
for item in generalData:
         try:
            print(item.text)
      
            print("")
      
         except:
              pass   

					
					
