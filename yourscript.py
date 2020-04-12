""" .......................yourscript embedded in the new environment variable i.e. venv ............................................ """
import requests
import re
import os
from bs4 import BeautifulSoup
import sys
import click

@click.command()
@click.option('--movie', prompt = True)
def cli(movie):
    base_url ='https://www.imdb.com/find?q={}+&ref_=nv_sr_sm'.format(movie)
    click.echo(base_url)
    req = requests.get(base_url)
    soup = BeautifulSoup(req.content, 'html.parser')
    title =soup.find_all('table', {"class":"findList"})[0]
    p=len(title)
    click.echo(title.text)
    click.echo('Scraping the first one if the scraping is wrong retype as it is shown')
    click.echo(p)
    anchor = title.find_all(lambda tag: tag.name =='a' and tag.get('href') and tag.text)
    
    fom = len(anchor) *2
    #print(anchor)

    if len(anchor)>=3:

        for x in range(1,fom,2):
            try:
                b = title.find_all('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+'))[x]
                if x ==1 :
                    extract = b.attrs['href']
    #
                else:
                    print("____")
    #
            except IndexError:
                break

    else:
        for x in range(1,fom,2):
            b = title.find_all('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+'))[x]
            if x ==1:
                extract = b.attrs['href']


            else:
                print(".........")

    extract="https://www.imdb.com{}".format(str(extract))



    final =requests.get(extract,headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})

    soup1= BeautifulSoup(final.content, 'html.parser')

    movie_details = soup1.select("#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper")[0].text
    print(movie_details)

    movie_rating = soup1.select("#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span")[0].text
    print("The rating for this movie is {}".format(movie_rating))

    summary = soup1.find('div',attrs={"class":"summary_text"}).get_text()

    print(summary)
