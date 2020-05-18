# ThisWordDoesNotExist_Bot
Python script/bot to automatically scrape data from [thisworddoesnotexist.com](https://www.thisworddoesnotexist.com/) made by [Thomas Dimson](https://github.com/turtlesoupy) and upload them to Instagram.
## Getting Started
There are two easy ways to use the script.
 - Clone project then input your Instagram data and run "bot.py". Running the script will cause it to act like a bot which periodically fetches the data and publishes stuff on the inserted profile.
```
username, password = "INSTAGRAM USERNAME", "INSTAGRAM PASSWORD"
postCaption = "INSTAGRAM POST CAPTION"
scheduleMinutes = *INSERT NUMBER OF MINUTES*
pictureSize = (width, height)
outputFileName = "outputFileName.jpg"
```
 - Clone project and edit "bot.py" to your liking. Removing the scheduler will cause the script to no longer act like a bot.
```
# Schedule
    schedule.every(scheduleMinutes).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
```
### Prerequisites
The "requirements.txt" file contains any Python dependencies. You can install them by running this command:
```
pip3 install -r requirements.txt
```
## Built With
- [Requests](https://requests.readthedocs.io/en/master/) - HTTP library for Python.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML documents analysis.
- [PIL](https://pillow.readthedocs.io/en/stable/) - Python Image Library.
- [Instabot](https://github.com/instagrambot/instabot) - Instagram Python API Wrapper.
- [Schedule](https://schedule.readthedocs.io/en/stable/) - Python job scheduling for humans.
### Creators
[Andrea Lin](https://github.com/nilaerdna/) & [Mattia Ferrari](https://github.com/IlSassone)
