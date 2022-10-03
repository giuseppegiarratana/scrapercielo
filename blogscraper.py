from email import header
import re
from turtle import title
import requests
from bs4 import BeautifulSoup


def blogscaper():
    articlelist=[]
    url ="https://www.aranzulla.it/"

    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

    r = requests.get(url, headers=headers)

    soup=BeautifulSoup(r.content, features="lxml")
    articles=soup.find_all("article", class_="contentPreview column")
    for item in articles:
        title=item.find({"a": "href"})
    #  articolo=item.find("div",class_="post").text
        # article={
        #     "title": title,

        # }

        articlelist.append(title)
        print(title)
    
    return articlelist

