import urllib.request
from bs4 import BeautifulSoup

#takes the site you want to scrape as a parameter
class Scraper:
    def __init__(self, site):
        self.site = site
    #This function does the actual scraping
    def scrape(self):
        #this makes a request to the website
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        #Uses BeautifulSoup to search the website html to find all the tags with urls
        sp = BeautifulSoup(html, parser)
        for tag in sp.find+all("a"):
            url = tag.get("href")
            print("\n" + url)


news = "https://news.google.com"
Scraper(news).scrape()