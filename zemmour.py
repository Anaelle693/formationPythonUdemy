from bs4 import BeautifulSoup
import urllib.request
import csv


urlpage = "https://www.bfmtv.com/politique/"
link = []

def get_Zemmour():
    page = urllib.request.urlopen(urlpage)
    soup = BeautifulSoup(page, "html.parser")
    articles = soup.find_all("article", class_="content_item")
    
    for article in articles:
      data = article.find("h3", class_="content_item_title")
      articleSTR = str(data)
      linkvalidate = articleSTR.replace("<h3 class=\"content_item_title\">", "").replace("</h3>", "")
      link.extend([linkvalidate])
      print(link)

get_Zemmour()