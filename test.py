from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper
import textwrap
import time

# 0: background color; 1: text color; 2: type and example color
colors = [(8, 8, 45, 255), (255, 255, 255, 255), (255, 255, 255, 128)]

# New image, size 1080x1080, solid color HEX = #08082d // RGBa(8, 8, 45, 255)
img = Image.new('RGBA', (1080, 1080), colors[0])

fontHeavy = "font/Heavy.ttf"
fontRegular = "font/Regular.ttf"
fontRegularItalic = "font/RegularItalic.ttf"

# Scraped Data
scraper = Scraper()

# Lists
# Type, Title, Syllables, Definition, Example
dimensionsList = [13, 64, 16, 16, 16]
fontsList = [fontRegular, fontHeavy, fontHeavy, fontRegular, fontRegularItalic]
colorsList = [colors[2], colors[1], colors[1], colors[1], colors[2]]
sizeMultiplier = 2
heightList = [0]

imgWidth, imgHeight = img.size

listCounter = 0
currentY = 0

def drawMultipleLineText(text, fontFile, fontSize, color, iterator):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)
    
    global listCounter
    global currentY
    # Image Size

    textY = 0

    lines = textwrap.wrap(text, width=60)

    for index, line in enumerate(lines):
        lineWidth, lineHeight = font.getsize(line)

        # Calculate Current Line Coordinates
        currentX = ((imgWidth - lineWidth) / 2)
        currentY +=  heightList[listCounter]
        draw.multiline_text((currentX, currentY), line, font=font, fill=color)
        # img.show()
        print(listCounter)
        listCounter+=1

def textHeight(text, fontFile, fontSize, color, iterator):
    font = ImageFont.truetype(fontFile, fontSize)
    lines = textwrap.wrap(text, width=60)
    for line in lines:
        lineWidth, lineHeight = font.getsize(line)
        heightList.append(lineHeight)
    return sum(heightList)

def main():
    scraper.getContent()
    
    print ("Altezza immagini")
    for i, textString in enumerate(scraper.values):
        # print(i, textString)
        heightSum = textHeight(textString, fontsList[i], dimensionsList[i]*sizeMultiplier, colorsList[i], i+1)
    print(heightList)
    print("Somma altezze:", heightSum)

    global currentY

    currentY = (imgHeight - heightSum)/2

    for i, textString in enumerate(scraper.values):
        drawMultipleLineText(textString, fontsList[i], dimensionsList[i]*sizeMultiplier, colorsList[i], i+1)

    img.save("test.png")
    img.show()

if __name__ == "__main__":
    main()