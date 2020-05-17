# Generazione Immagine da caricare
from PIL import Image, ImageFont, ImageDraw
import textwrap

fontHeavy = "font/Heavy.ttf"
fontRegular = "font/Regular.ttf"
fontRegularItalic = "font/RegularItalic.ttf"
dimensionsList = [26, 128, 32, 32, 32]
fontsList = [fontRegular, fontHeavy, fontHeavy, fontRegular, fontRegularItalic]
colors = ["#08082D", "#FFFFFF", "#848496"]
colorsList = [colors[2], colors[1], colors[1], colors[1], colors[2]]

class Picture:
    def __init__(self, dimensions, text, outputFileName):
        # Creates Background Image
        self.image = Image.new('RGB', dimensions, colors[0])
        # Text that needs to be printed on the background
        self.text = text
        self.outputFileName = outputFileName
        self.heightList = [0]
        self.lineHeight()
        self.textHeight = sum(self.heightList)
        self.currentY = (dimensions[1] - self.textHeight) / 2
        self.lineCounter = 0

    def drawMultipleLineText(self, text, iterator):
        font = ImageFont.truetype(fontsList[iterator], dimensionsList[iterator])
        draw = ImageDraw.Draw(self.image)

        lines = textwrap.wrap(text, width=60)

        for line in lines:
            lineWidth = font.getsize(line)[0]

            # Calculates Current X Coordinates
            currentX = ((self.image.size[1] - lineWidth) / 2)

            # Gets and Calculates Y Coordinate
            self.currentY += self.heightList[self.lineCounter]
            draw.multiline_text((currentX, self.currentY), line, font=font, fill=colorsList[iterator])

            self.lineCounter += 1

    def drawAllText(self):
        for i, textString in enumerate(self.text):
            self.drawMultipleLineText(textString, i)

    def lineHeight(self):
        for i, textString in enumerate(self.text):
            font = ImageFont.truetype(fontsList[i], dimensionsList[i])
            lines = textwrap.wrap(textString, width=60)
            for line in lines:
                lineHeight = font.getsize(line)[1]
                self.heightList.append(lineHeight)

    def saveFile(self):
        self.image.save(self.outputFileName)
