from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper as Scrap
from datetime import datetime

# 0: background color; 1: text color; 2: type and example color
colors = [(8, 8, 45, 255), (255, 255, 255, 255), (255, 255, 255, 128)]

# New image, size 1080x1080, solid color HEX = #08082d // RGBa(8, 8, 45, 255)
img = Image.new('RGBA', (1080, 1080), colors[0])

fontHeavy = "font/Heavy.ttf"
fontRegular = "font/Regular.ttf"
fontRegularItalic = "font/RegularItalic.ttf"

sizeMultiplier = 2

# Scraped Data
scraper = Scrap()

def drawText(text, coords, fontFile, fontSize=10, color=(255, 255, 255, 128)):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)
    draw.multiline_text(coords, text, font=font, fill=color, align="left")


if __name__ == "__main__":
    scraper.getContent()
    print(scraper.data)
    
    # Type
    drawText(scraper.data['type'], (30, 10), fontRegular, fontSize=13*sizeMultiplier, color=colors[2])
    # Title
    drawText(scraper.data['word'], (30, 15), fontHeavy, fontSize=64*sizeMultiplier, color=colors[1])
    # Syllables
    drawText(scraper.data['syllables'], (30, 150), fontHeavy, fontSize=16*sizeMultiplier, color=colors[1])
    # Definition
    drawText(scraper.data['definition'], (30, 500), fontRegular, fontSize=16*sizeMultiplier, color=colors[1])
    # Example
    drawText(scraper.data['example'], (30, 650), fontRegularItalic, fontSize=16*sizeMultiplier, color=colors[2])
    
    img.save("test.png")
    img.show()
