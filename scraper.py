from selenium import webdriver
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self):
        self.result = None
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
        self.data = {}
    
    def stringClean(self, x):
        x= x.replace("\n", "")
        x = x.strip()

        return x
    
    def getContent(self):
        self.driver.get("https://www.thisworddoesnotexist.com/")
        self.result = self.driver.page_source
        self.driver.quit()
        self.getDiv()
        
    def getDiv(self):
        soup = BeautifulSoup(self.result)
        self.data['title'] = soup.find('div', attrs={'id':'definition-word'}).text
        self.data['type'] = self.stringClean(soup.find('div', attrs={'id':'definition-pos'}).text)
        self.data['syllables'] = self.stringClean(soup.find('div', attrs={'id':'definition-syllables'}).text)
        self.data['definition'] = soup.find('div', attrs={'id':'definition-definition'}).text
        self.data['example'] = soup.find('div', attrs={'id': 'definition-example'}).text
