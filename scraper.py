from selenium import webdriver
from bs4 import BeautifulSoup

class Scraper:
    
    def __init__(self):
        self.result = None
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
        self.div = None
    
    def getContent(self):
        self.driver.get("https://www.thisworddoesnotexist.com/")
        self.result = self.driver.page_source
        self.getDiv()
        
    def getDiv(self):
        soup = BeautifulSoup(self.result)
        self.div = soup.find('div', attrs={'class':'inner'})
