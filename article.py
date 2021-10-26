import re
from bs4 import BeautifulSoup
import urllib.request
import csv
import json


urlpage = "https://www.bfmtv.com/politique/"
link = []
def get_Zemmour():
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, "html.parser")
    articles = soup.find_all("article", class_="content_item")
    
    search = input("Que voulez vous chercher : ")
    for article in articles:
      data = article.find("h3", class_="content_item_title")
      articleSTR = str(data)
      linkvalidate = articleSTR.strip("<h3 class=\"content_item_title\"> </h3>")
      
      if linkvalidate.find(search) != -1:
        global link
        link.extend([linkvalidate])
      else:
        pass
      with open("z.json", "w") as f:
        json.dump(link, f, indent=4)
      with open("z.json", "r") as f:
        link = json.load(f)
    print(link)   

get_Zemmour()