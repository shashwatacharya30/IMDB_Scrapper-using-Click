import re
from bs4 import BeautifulSoup
import requests
import sys
import os

keyword = input("Enter the movie that we are about the search:")
print("The movie that is being requested is {}".format(keyword))

base_url ='https://www.imdb.com/find?q={}+&ref_=nv_sr_sm'.format(keyword)
#print(base_url)
req = requests.get(base_url)
soup = BeautifulSoup(req.content, 'html.parser')

#this section will show the value that the website will reflect once you put the key word
#--------------------section Starts----------------------------
title =soup.find_all('table', {"class":"findList"})[0]

#print(title.prettify())


#print(len(title))
p=len(title)
#print(title.text)

anchor = title.find_all(lambda tag: tag.name =='a' and tag.get('href') and tag.text)
#print(type(anchor))
#print(len(anchor))
fom = len(anchor) *2
#print(anchor)

if len(anchor)>=3:

    for x in range(1,fom,2):
        try:
            b = title.find_all('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+'))[x]
            if x ==1 :
                extract = b.attrs['href']
#                print(extract)
#                print(type(extract))
            else:
                print("____")
#                print(b.attrs['href'], b.text)
        except IndexError:
            break

else:
    for x in range(1,fom,2):
        b = title.find_all('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+'))[x]
        if x ==1:
            extract = b.attrs['href']
            print(extract)
            print(type(extract))
        else:
            print(b.attrs['href'], b.text)

extract="https://www.imdb.com{}".format(str(extract))


print(extract)
final =requests.get(extract,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})
print(final)
soup1= BeautifulSoup(final.content, 'html.parser')
#print(soup1.prettify())
movie_details = soup1.select("#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper")[0].text
print(movie_details)

movie_rating = soup1.select("#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span")[0].text
print(movie_rating)
#print(len(movie_title_name))

#plot = soup1.select("#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div.summary_text")

#print(type(plot))

summary = soup1.find('div',attrs={"class":"summary_text"}).get_text()

print(summary)




"""
-------Locating only that tag which contains all the name and the tag ------- but in a list form not in a TAG form
title_name=title.find_all('td', {"class":"result_text"})
print(len(title_name))
print(type(title_name))
print(title_name)




......................................converting the title_name from <class.bs4.element.ResultSet> insto <class 'str'>.................................
title_name = ' '.join(map(str, title_name))
print(type(title_name))

"""
