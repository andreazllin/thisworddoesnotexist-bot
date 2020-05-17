from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper as Scrap
# Per convertire i file per i font in ttf: https://onlinefontconverter.com/

fontFile = "font/Helvetica.ttf"
img = Image.new('RGB', (1080, 1080), (8, 8, 45))
scraper = Scrap()
def writeText(text, x, y, fontName, fontSize=10, color="white"):
    font = ImageFont.truetype(fontFile, fontSize)
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, font=font, fill=color)

if __name__ == "__main__":
        # New image, size 1080x1080, solid color HEX = #08082d // RGB(8, 8, 45)
    scraper.getContent()
    writeText(scraper.data['title'], 10, 10, fontFile, fontSize=75, color="white")
    img.show()
