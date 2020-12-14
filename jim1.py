#<span data-placement="top" title=

#  this pulls names of people's from the scsa world challenge squad list even if they say reserved when viewed in practiscore   .

import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from html.entities import name2codepoint

count =0
import time
import sys
from os import system
print ("jd starting jim1.py")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
#        print("Start tag:", tag)
        for i in range(len(attrs)  )  :
#            if (i==2 or i==3 or i==7):
             if ( i==7):
                print( i  , attrs[i])
            
               
print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
               

#system('say emily  do you want dessert  ' + str(10)  )
print ("Start : %s"  % time.ctime())
url ='https://practiscore.com/world-speed-shooting-championship-2021-presented-by-psa/squadding'
print ( url )

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')


"""
<span data-placement="top" disabled="disabled" id="squad_452038_1_117990" name="squad_452038_1_117990" placeholder="reserved" rel="1" style="background-color: #fcf8e3;" title="Zack Jones, JR (PCC Optic)">
<small class="text-muted">Reserved</small>
</span>

"""

#print(soup.select_one("span[title*=Kurt]"))

#jjj =str ( soup.select_one('span[data-placement="top"]')  )

parser = MyHTMLParser()

#for kkk in soup.find_all('span', {'data-placement':'top'}):
for iteration, kkk in  enumerate ( soup.find_all('span', {'data-placement':'top'})  ) :

    #print kkk  # raw html with span tags
    print ( parser.feed( str(kkk)  ) )
    #print ( iteration+1)
                
print ("Total")
print ( str(iteration+1))



quit()





"""

<span data-placement="top" disabled="disabled" id="squad_452038_1_117990" name="squad_452038_1_117990" placeholder="reserved" rel="1" style="background-color: #fcf8e3;" title="Zack Jones, JR (PCC Optic)">
<small class="text-muted">Reserved</small>
</span>
"""



"""


print ("aaaaa")
aa=soup.find('div', {'class' :'squadBox'}).text
print (aa )
"""


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

"""
