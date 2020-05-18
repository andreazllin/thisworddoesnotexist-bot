from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper
from instabot import Bot
import textwrap
import time
import schedule
import os

# RGBA to RGB converter -> https://borderleft.com/toolbox/rgba/
# RGB to HEX - > https://www.color-hex.com/
# 0: background color (8, 8, 45, 255); 1: text color (255, 255, 255, 255); 2: type and example color (255, 255, 255, 128)
colors = ["#08082D", "#FFFFFF", "#848496"]

usrnm, pswrd = "USERNAME HERE", "PASSWORD HERE"

# New image, size 1080x1080, solid color HEX = #08082d // RGB(8, 8, 45)
img = Image.new('RGB', (1080, 1080), colors[0])

# File Names
fontHeavy = "font/Heavy.ttf"
fontRegular = "font/Regular.ttf"
fontRegularItalic = "font/RegularItalic.ttf"
outputFileName = "outputImage.jpg"

# Scraped Data
scraper = Scraper()

# Lists
# Type, Title, Syllables, Definition, Example
dimensionsList = [13, 64, 16, 16, 16]
fontsList = [fontRegular, fontHeavy, fontHeavy, fontRegular, fontRegularItalic]
colorsList = [colors[2], colors[1], colors[1], colors[1], colors[2]]
sizeMultiplier = 2
heightList = [0]

# Image Size
imgWidth, imgHeight = img.size

# heightList iterator
listCounter = 0

# Y position
currentY = 0

def drawMultipleLineText(text, fontFile, fontSize, color, iterator):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)

    global listCounter
    global currentY

    lines = textwrap.wrap(text, width=60)

    for index, line in enumerate(lines):
        lineWidth, lineHeight = font.getsize(line)

        # Calculates Current X Coordinates
        currentX = ((imgWidth - lineWidth) / 2)

        # Gets and Calculates Y Coordinate
        currentY += heightList[listCounter]
        draw.multiline_text((currentX, currentY), line, font=font, fill=color)

        listCounter += 1


def textHeight(text, fontFile, fontSize, color, iterator):
    font = ImageFont.truetype(fontFile, fontSize)
    lines = textwrap.wrap(text, width=60)
    for line in lines:
        lineWidth, lineHeight = font.getsize(line)
        heightList.append(lineHeight)
    return sum(heightList)


def resetGlobals():
    global listCounter
    global currentY
    global heightList
    global img
    global scraper
    listCounter = 0
    currentY = 0
    heightList = [0]
    scraper = Scraper()
    img = Image.new('RGB', (1080, 1080), colors[0])
    os.remove(outputFileName + ".REMOVE_ME")

def postOnInstagram():
    bot.upload_photo(outputFileName, caption="A word that does not exist; it was invented, defined and used by a machine learning algorithm.")

def main():
    print("SONO NEL MAIN")
    scraper.getContent()

    for i, textString in enumerate(scraper.values):
        # print(i, textString)
        heightSum = textHeight(
            textString, fontsList[i], dimensionsList[i]*sizeMultiplier, colorsList[i], i+1)

    global currentY

    currentY = (imgHeight - heightSum)/2

    for i, textString in enumerate(scraper.values):
        drawMultipleLineText(
            textString, fontsList[i], dimensionsList[i]*sizeMultiplier, colorsList[i], i+1)
    
    print("FINITO DI GENERARE L'IMMAGINE")
    img.save(outputFileName)
    postOnInstagram()
    img.close()
    resetGlobals()
    # img.show()


if __name__ == "__main__":
    # Bot config
    bot = Bot()
    bot.login(username=usrnm, password=pswrd)
    main()
    schedule.every(2).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
