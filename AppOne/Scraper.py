# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:44:54 2018

@author: Dinesh
"""
import urllib
from bs4 import BeautifulSoup


#string=input()
def func(string):
    page="https://www.imdb.com/find?ref_=nv_sr_fn&q=&s=all"

    string= string.replace(' ','+')
    search_page=page.split('q=')[0]+"q="+string+"&s=all"
    search_page = urllib.request.urlopen(search_page)

    soup1 = BeautifulSoup(search_page, 'html.parser')

    x1=soup1.find_all("td", class_="primary_photo")
    x1=str(str(x1[0]).split("title/"))

    title=x1[43:52]

    page='https://www.imdb.com/title/' +title
    page = urllib.request.urlopen(page)
    soup = BeautifulSoup(page, 'html.parser')

    imgs=[]
    for link in soup.find_all('img'):
        imgs.append(link.get('src'))

    return (imgs[2].split('_V1_')[0]+"_V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg"),(soup.find_all(class_="summary_text")[0].text.strip()),(soup.find_all(class_="rating")[0].text.strip())
