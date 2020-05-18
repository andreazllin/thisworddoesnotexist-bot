from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_argument("--headless")

class Scraper:
    
    def __init__(self):
        self.result = None
        self.driver = webdriver.Chrome("./driver/chromedriver.exe", chrome_options=chrome_options)
        self.data = {}
        self.values = []

    def stringClean(self, x):
        x = x.replace("\n", "")
        x = x.strip()
        return x
    
    def getContent(self):
        self.driver.get("https://www.thisworddoesnotexist.com/")
        self.result = self.driver.page_source
        self.driver.quit()
        self.getDiv()
        
    def getDiv(self):
        soup = BeautifulSoup(self.result, features="html.parser")
        self.data['type'] = self.stringClean(soup.find('div', attrs={'id':'definition-pos'}).text)
        self.data['word'] = self.stringClean(soup.find('div', attrs={'id': 'definition-word'}).text)
        self.data['syllables'] = self.stringClean(soup.find('div', attrs={'id':'definition-syllables'}).text)
        self.data['definition'] = self.stringClean(soup.find('div', attrs={'id':'definition-definition'}).text)
        self.data['example'] = self.stringClean(soup.find('div', attrs={'id': 'definition-example'}).text)
        self.values = self.data.values()
        print(self.values)
        if (len(self.data['word']) > 15):
            self.driver.refresh()
            print("Word longer than 15 characters!")
            self.getContent()
