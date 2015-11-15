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

def generateCard1():
  card = getBlankCard()
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
  paintBackgroundOrange(card)
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
  addTextWithStyle(card, startX, startY, text, textStyle, green)

# Apply the turkey holding the sign to a card.
def applyTurkey1(card):
  turkeyPic = makePicture("turkey1.jpg")
  # Apply to center of card
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

# Color the entire pic a particular color.
def paintBackgroundOrange(card):
  bgColor = makeColor(255, 153, 0)
  for x in range(0, getWidth(card)-1):
    for y in range(0, getHeight(card)-1):
      pixel = getPixel(card, x, y)
      setColor(pixel, bgColor)
