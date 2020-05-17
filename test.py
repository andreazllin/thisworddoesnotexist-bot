from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper as Scrap
from datetime import datetime

# New image, size 1080x1080, solid color HEX = #08082d // RGB(8, 8, 45)
img = Image.new('RGB', (1080, 1080), (8, 8, 45))

# White Text = rgb(255, 252, 255)
# Grey Text = rgb(132, 132, 150)
fontHeavy = "font/Heavy.ttf"
fontRegular = "font/Regular.ttf"
fontRegularItalic = "font/RegularItalic.ttf"

sizeMultiplier = 2

# Scraped Data
scraper = Scrap()

def drawText(text, coords, fontFile, fontSize=10, color="white"):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)
    draw.text(coords, text, font=font, fill=color)



if __name__ == "__main__":
    scraper.getContent()
    print(scraper.data)
    
    # Type
    drawText(scraper.data['type'], (10, 10), fontRegular, fontSize=13*sizeMultiplier, color="gray")
    # Title
    drawText(scraper.data['word'], (10, 15), fontHeavy, fontSize=64*sizeMultiplier, color="white")
    # Syllables
    drawText(scraper.data['syllables'], (10, 50), fontHeavy, fontSize=16*sizeMultiplier, color="white")
    # Definition
    drawText(scraper.data['definition'], (10, 100), fontRegular, fontSize=16*sizeMultiplier, color="white")
    # Example
    drawText(scraper.data['example'], (10, 150), fontRegularItalic, fontSize=16*sizeMultiplier, color="white")
    
    img.save("test.png")
    img.show()
