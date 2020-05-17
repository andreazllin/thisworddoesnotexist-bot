from selenium import webdriver

class Scraper:
    
    def __init__(self):
        self.result = None
        self.driver = webdriver.Chrome("./driver/chromedriver.exe")
        self.div = None
    
    def getContent(self):
        self.driver.get("https://www.thisworddoesnotexist.com/")
        self.result = self.driver.page_source
        
    def getDiv(self):
        self.div ="sos"
