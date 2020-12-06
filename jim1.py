import requests
from bs4 import BeautifulSoup

import time
import sys
from os import system
print ("aggg")


#print ("Start : %s"  time.ctime())

url = 'https://practiscore.com/world-speed-shooting-championship-2020/squadding'
print ( url )

#res = requests.get(url)


html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

print ("jjj")





#html = open("medium.html").read()
#soup = BeautifulSoup(html_text)

mydivs = soup.find('div', {'class' :'squadBox'}).text
print ( mydivs )

#for div in mydivs:
    #print div
 #   print ("dddd")





tag = soup.find( text="Empty")


print ("aaaaa")
aa=soup.find('div', {'class' :'squadBox'}).text
print (aa )



#print tag.find_parent('div')











"""
table = soup.find('div', attrs={'class': 'content'})

rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    for td in cols:
        text = td.find(text=True) + ';'
        print text,
    print







tables = [
    [
        [td.get_text(strip=True) for td in tr.find_all('td')]
        for tr in table.find_all('tr')
    ]
    for table in soup.find_all('table')
]





#print(soup.title)
print (soup.title.text)






#text = soup.get_text()

print ("end ")

"""
