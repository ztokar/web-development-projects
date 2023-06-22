import requests
from bs4 import BeautifulSoup

response=requests.get("https://news.ycombinator.com/news")

yc_webpage=response.text  #isn't there also a JSON of this available?

soup=BeautifulSoup(yc_webpage,"html.parser")

all_titles=soup.select(selector=".titleline")
for title in all_titles:
    print(title.getText())


all_links=soup.select(selector=".sitestr") #get("href")
for link in all_links:
    print(link.getText())

article_upvote=soup.select(selector=".score") #(.find(name=span,class=score))
for score in article_upvote:
    print(score.getText())

