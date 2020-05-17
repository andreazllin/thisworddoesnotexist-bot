from PIL import Image, ImageFont, ImageDraw
from scraper import Scraper as S
# Per convertire i file per i font in ttf: https://onlinefontconverter.com/

def writeText(text, x, y, fontName, fontSize = 10, color = "white"):
    font = ImageFont.truetype(fontName, fontSize)
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, font=font, fill=color)
    pass

def main():
    inputFile = "imgs/bg.png"
    outputFile = "imgs/sasso.png"
    fontName = "font/Helvetica.ttf"
    image = Image.open(inputFile)
    scraper = S()
    scraper.getContent()
    print(scraper.data)
    writeText("manifestogenesis", 10, 10, fontName, fontSize = 500, color = "white")
    image.save("sasso_finale.png")
    image.show()
    pass

if __name__ == "__main__":
    main()
