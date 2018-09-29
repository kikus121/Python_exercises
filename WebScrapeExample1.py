print("")
print("")
print("")


import requests
from bs4 import BeautifulSoup
r= requests.get("https://www.yellowpages.com/search?search_terms=Coffee+Shops&geo_location_terms=7+Dublin%2C+Kingston%2C+OK")#Gets Html code from web
soup = BeautifulSoup(r.content,"html.parser")#Formats html to be readable. "html.parser" is required this time for some reason

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HTML CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

print(soup.prettify())#Prints html code

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CLASS 'a' LIST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

x=soup.find_all("a")# creats a list of links to class "a"
print(x)#Prints lin ks to something

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!SEPERATE BY LINE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

for link in x: 
    print(link)#Seperateslinks by lines
    
print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!HREF!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

for link in x: 
    print(link.get("href"))#Gets href (LINKS)

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TEXT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

for link in x: 
    print(link.text)#Gets text

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TEXT + href!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")

for link in x: 
    print(link.text,link.get("href"))#Gets text

print("")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!TEXT + href nice format!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("")


for link in x: 
    print("a href={}>{}</a".format(link.get("href"),link.text))#Gets text

