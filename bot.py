from scraper import Scraper
from picture import Picture
from instabot import Bot
import schedule
import time
import os

username, password = "INSTAGRAM USERNAME", "INSTAGRAM PASSWORD"
postCaption = "INSTAGRAM POST CAPTION"
scheduleMinutes = 10
pictureSize = (1080, 1080)
outputFileName = "outputImage.jpg"

def main():
    scraper = Scraper()
    scraper.getContent()

    newPost = Picture(pictureSize, scraper.values, outputFileName)
    newPost.drawAllText()
    newPost.saveFile()

    postOnInstagram()
    os.remove(outputFileName + ".REMOVE_ME")
    newPost.image.close()
    
def postOnInstagram():
    bot.upload_photo(outputFileName, caption=postCaption)

if __name__ == "__main__":
    # Bot config
    bot = Bot()
    bot.login(username=username, password=password)

    main()

    # Schedule
    schedule.every(scheduleMinutes).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
