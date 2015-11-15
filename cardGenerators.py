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
"""

def generateCard1():
  card = getBlankCard()
  return card
  
def generateCard2():
  card = getBlankCard()
  return card
  
def generateCard3():
  card = getBlankCard()
  return card
  
def generateCard4():
  card = getBlankCard()
  return card
  
def getBlankCard():
  # Create 5x7 card
  return makeEmptyPicture(1260, 900)