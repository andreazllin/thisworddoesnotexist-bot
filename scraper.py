import requests
from bs4 import BeautifulSoup

URL = 'https://www.thisworddoesnotexist.com/'

class Scraper:
    
    def __init__(self):
        self.result = None
        self.data = {}
        self.values = []

    def stringClean(self, x):
        x = x.replace("\n", "")
        x = x.strip()
        return x
    
    def getContent(self):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, features="html.parser")
        self.data['type'] = self.stringClean(soup.find('div', attrs={'id':'definition-pos'}).text)
        self.data['word'] = self.stringClean(soup.find('div', attrs={'id': 'definition-word'}).text)
        self.data['syllables'] = self.stringClean(soup.find('div', attrs={'id':'definition-syllables'}).text)
        self.data['definition'] = self.stringClean(soup.find('div', attrs={'id':'definition-definition'}).text)
        self.data['example'] = self.stringClean(soup.find('div', attrs={'id': 'definition-example'}).text)
        self.values = self.data.values()
        print(self.values)
        if (len(self.data['word']) > 15):
            print("Word longer than 15 characters!")
            self.getContent()
