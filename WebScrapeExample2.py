import requests
from bs4 import BeautifulSoup

url="https://www.yellowpages.com/search?search_terms=Coffee+Shops&geo_location_terms=7+Dublin%2C+Kingston%2C+OK"
r= requests.get(url)#Gets Html code from web
soup = BeautifulSoup(r.content,"html.parser")#Formats html to be readable. "html.parser" is required this time for some reason
links=soup.find_all("a")

#for link in links:
    #print("a href={}>{}</a".format(link.get("href"),link.text))#Gets text
 
general_data=soup.find_all("div",{"class": "info"})#gets 'div class=info' from html code
#print(general_data)

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Text!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")


#for item in general_data:
    #print(item.text)#Gets text

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Contents!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")


#for item in general_data:
    #print(item.contents)#Gets text

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Contents list with index!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Name of cafee!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


for item in general_data:
    print(item.contents[0].text)#Gets text from info class firs subclass eg its a list of clases
    
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Contact info of cafee!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

for item in general_data:
    print(item.contents[1].text)#Gets text from info class firs subclass eg its a list of clases


print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Gets just name!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")


for item in general_data:
    try:
        print(item.contents[0].find_all(("a",{"class":"business-name"}))[0].text)#item.contents[index].find_all("tag",{"class":"class name"}
    except:
        pass

#for item in general_data:
    #print(item.contents[0].find_all(("a",{"class":"name"})))#item.contents[index].find_all("tag",{"class":"class name"}

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Gets just adress!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

for item in general_data:
    try:
        print(item.contents[0].find_all(("p",{"class":"adr"}))[1].text)#item.contents[index].find_all("tag",{"class":"class name"}
    except:
        pass

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Gets just phone!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

for item in general_data:
    try:
        print(item.contents[0].find_all(("p",{"itempromp":"telephone"}))[0].text)#item.contents[index].find_all("tag",{"class":"class name"}
    except:
        pass

