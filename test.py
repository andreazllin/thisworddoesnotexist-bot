from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper
import textwrap

# 0: background color; 1: text color; 2: type and example color
colors = [(8, 8, 45, 255), (255, 255, 255, 255), (255, 255, 255, 128)]

# New image, size 1080x1080, solid color HEX = #08082d // RGBa(8, 8, 45, 255)
img = Image.new('RGBA', (1080, 1080), colors[0])

fontHeavy = "font/Heavy.ttf"
fontRegular = "font/Regular.ttf"
fontRegularItalic = "font/RegularItalic.ttf"

# Scraped Data
scraper = Scraper()

"""
def drawText(text, coords, fontFile, fontSize, color=(255, 255, 255, 128)):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)
    draw.text(coords, text, font=font, fill=color, align="left")
"""


def drawMultipleLineText(text, fontFile, fontSize, color=(255, 255, 255, 128), iterator=1):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)

    # Image Size
    imgWidth, imgHeight = img.size

    textY = 50 # Y position where it starts

    lines = textwrap.wrap(text, width=60)

    for line in lines:
        lineWidth, lineHeight = font.getsize(line)

        print(font.getsize(line))
        draw.multiline_text(((imgWidth - lineWidth) / 2, 100 + (50*iterator)), line, font=font, fill=color)
        lastY = lineHeight

# Lists
# Type, Title, Syllables, Definition, Example
dimensionsList = [13, 64, 16, 16, 16]
fontsList = [fontRegular, fontHeavy, fontHeavy, fontRegular, fontRegularItalic]
colorsList = [colors[2], colors[1], colors[1], colors[1], colors[2]]
sizeMultiplier = 2
heightList = []


def textHeight(text, fontFile, fontSize, color=(255, 255, 255, 128), iterator=1):
    font = ImageFont.truetype(fontFile, fontSize)
    lines = textwrap.wrap(text, width=60)
    for line in lines:
        lineWidth, lineHeight = font.getsize(line)
        heightList.append(lineHeight)

def main():
    scraper.getContent()

    for i, textString in enumerate(scraper.values):
        # print(i, textString)
        textHeight(textString, fontsList[i], dimensionsList[i]*sizeMultiplier, color=colorsList[i], iterator=i+1)
        # drawMultipleLineText(textString, fontsList[i], dimensionsList[i]*sizeMultiplier, color=colorsList[i], iterator=i+1)

    print(heightList)

    #img.save("test.png")
    #img.show()

if __name__ == "__main__":
    main()
