"""
CSUMB CST 205: Multimedia Design and Programming
Lab #7 Homemade Thanksgiving

Team #6 - BITsoft: 
  Ashley Wallace
  John Lester
  Matthew Valancy (Crenshaw)
  Brittany Mazza
  
Notes:
  * All of the functions below rely on the 'mediaPath' variable being set
    correctly. Ensure 'mediaPath' is set to the correct directory 
    ('originals') prior to calling each function. This can be done in the
    console by calling 'setMediaPath', like:
      # OSX
      mediaPath = setMediaPath("YOUR_PATH_HERE/HomemadeThanksgivingCards/originals/")
      # or Windows
      mediaPath = setMediaPath("YOUR_PATH_HERE\HomemadeThanksgivingCards\originals\")
    This allows us to simply call 
    "makePicture("{image in original folder}")" to get the image we'd like
    to use.
    
Requirements for each card:
  * Contain a message (text).
  * At least three different images.
"""

def generateCard1(): #Matt V
  greenScreen = [50, 255, 50] # R G B values for green screen
  colorPrecision = 100 # how close the colors has to be to remove the alpha
  card = makePicture(getMediaPath("fatTurkey.jpg"))
  santas = makePicture(getMediaPath("santa.jpg"))
  dragon = makePicture(getMediaPath("dinosaur.jpg"))
  flamethrower = makePicture(getMediaPath("flamethrower.jpg"))
  
  textA = "Happy Thanksgiving! No, it's not Christmas yet."
  textB = "-Matt"
  
  pyCopyA(santas, card, 0, 290, greenScreen[0], greenScreen[1], greenScreen[2], 200)    
  pyCopyA(flamethrower, card, 140, 510, greenScreen[0], greenScreen[1], greenScreen[2], 200)    
  pyCopyA(dragon, card, -500, 400, greenScreen[0], greenScreen[1], greenScreen[2], 200)    

  addTextWithStyle(card, 60, 381, textA, makeStyle(serif, bold, 24))
  addTextWithStyle(card, 371, 420, textB, makeStyle(serif, bold, 24))
  
  return card
  
def generateCard2():
  card = getBlankCard()
  return card
  
def generateCard3():
  card = getBlankCard()
  applyPumpkinPie(card)
  return card
  
def generateCard4():
  card = getBlankCard()
  addSunshine(card)
  addGrass(card)
  applyTurkey1(card)
  addQuestionableHappyThanksgivingText(card)
  return card

"""
Methods below are used to generate all cards.
"""
def getBlankCard():
  # Create 5x7 card
  return makeEmptyPicture(945, 675)


"""
Methods below are used to generate card 1.
"""

# Function: python copy with alpha, copy source image to target image and remove transparent pixels
# Params: source image, target image, target x for 0, target y for 0 
# Returns: Resized picture
def pyCopyA(source, target, targetX, targetY, alphaR, alphaG, alphaB, precision):
  targetWidth = target.getWidth()
  targetHeight = target.getHeight()

  for y in range( 0, source.getHeight() ): # work from top to bottom
    if (y + targetY < targetHeight) and (y + targetY > 0): #Y range check so we can go crazy and not worry
      for x in range( 0, source.getWidth() ):
        if (x + targetX < targetWidth) and (x + targetX > 0): #X range check so we can go crazy and not worry
          sourcePixel = getPixel(source, x, y)
          sourceColor = getColor(sourcePixel)
          if ( abs(sourceColor.getRed() - alphaR) + abs(sourceColor.getBlue() - alphaB) + abs(sourceColor.getGreen() - alphaG) ) > precision: 
            destPixel = getPixel(target, x + targetX, y + targetY)
            destPixel.setColor(sourceColor)    


"""
Methods below are used to generate card 2.
"""

"""
Methods below are used to generate card 3.
"""
# Apply pumpkin pie to card.
def applyPumpkinPie(card):
  piePic = makePicture("pumpkin-pie.jpg")
  # Apply to bottom right corner of card
  startX = getWidth(card) - getWidth(piePic)
  startY = getHeight(card) - getHeight(piePic)
  for x in range(0, getWidth(piePic)-1):
    for y in range(0, getHeight(piePic)-1):
      piePixel = getPixel(piePic, x, y)
      piePixelColor = getColor(piePixel)
      setColor(getPixel(card, startX + x, startY + y), piePixelColor)

"""
Methods below are used to generate card 4.
"""
# Add "Happy Thanksgiving?" text to card.
def addQuestionableHappyThanksgivingText(card):
  text = "Happy Thanksgiving?"
  textStyle = makeStyle(serif, bold, 13)
  startX = (getWidth(card)/20)*11
  startY = (getHeight(card)/20)*7
  textColor = makeColor(153, 0, 0)
  addTextWithStyle(card, startX, startY, text, textStyle, textColor)

# Apply the turkey holding the sign to a card.
def applyTurkey1(card):
  turkeyPic = makePicture("turkey1.jpg")
  # Apply to center of card.
  startX = (getWidth(card) - getWidth(turkeyPic))/2
  startY = (getHeight(card) - getHeight(turkeyPic))/2
  for x in range(0, getWidth(turkeyPic)-1):
    for y in range(0, getHeight(turkeyPic)-1):
      turkeyPixel = getPixel(turkeyPic, x, y)
      turkeyPixelColor = getColor(turkeyPixel)
      # Don't copy over white pixels to treat turkey background as if it
      # were transparent.
      if distance(turkeyPixelColor, white) > 0.75:
        cardPixel = getPixel(card, startX + x, startY + y)
        setColor(cardPixel, turkeyPixelColor)

# Add sunshine to card.
def addSunshine(card):
  sunshinePic = makePicture("sunshine.jpg")
  # Apply to top of card.
  for x in range(0, getWidth(sunshinePic)):
    for y in range(0, getHeight(sunshinePic)):
      pixel = getPixel(card, x, y)
      sunshineColor = getColor(getPixel(sunshinePic, x, y))
      setColor(pixel, sunshineColor)

# Add grass to card.
def addGrass(card):
  grassPic = makePicture("grass.png")
  # Apply to base of card.
  startY = getHeight(card) - getHeight(grassPic)
  for x in range(0, getWidth(grassPic)):
    for y in range(0, getHeight(grassPic)):
      grassColor = getColor(getPixel(grassPic, x, y))
      # Only color if grass image doesn't look black, which is how 
      # getColor interprets the transparency.
      if distance(grassColor, black) > 0.25:
        setColor(getPixel(card, x, startY + y), grassColor)

setMediaPath()
show(generateCard1())
show(generateCard2())
show(generateCard3())
show(generateCard4())