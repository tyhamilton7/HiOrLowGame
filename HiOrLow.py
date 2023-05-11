from graphics import *
import random
import time
#will use graphics.py for this

#CORRECT_GREEN
CORRECT_GREEN = color_rgb(55, 240, 55)
#CHECKMARK
checkbottom = Line(Point(130, 230), Point(229, 329)) 
checkbottom.setWidth(40)
checkbottom.setFill('white')

checktop = Line(Point(202, 330), Point(400, 130))
checktop.setWidth(40)
checktop.setFill('white')
#UP ARROW
regupArrowTri = Polygon(Point(250, 150),
                Point(225, 190),
                Point(275, 190))
regupArrowTri.setFill('yellow')
regupArrowTri.setOutline('yellow')
regupArrowLine = Rectangle(Point(243, 190),
                        Point(257, 300))
regupArrowLine.setOutline('yellow')
regupArrowLine.setFill('yellow')

#DOWN ARROW
regdownArrowTri = Polygon(Point(250, 300),
                        Point(225, 260),
                        Point(275, 260))
regdownArrowTri.setFill('red')
regdownArrowTri.setOutline('red')
regdownArrowLine = Rectangle(Point(243, 143),
                            Point(257, 270))
regdownArrowLine.setFill('red')


#title up arrow
titleupArrowTri = Polygon(Point(40, 140),
                Point(15, 180),
                Point(65, 180))
titleupArrowTri.setFill('yellow')
titleupArrowTri.setOutline('yellow')
titleupArrowLine = Rectangle(Point(33, 180),
                        Point(47, 290))
titleupArrowLine.setOutline('yellow')
titleupArrowLine.setFill('yellow')
#title down arrow
titledownArrowTri = Polygon(Point(460, 290),
                        Point(435, 250),
                        Point(485, 250))
titledownArrowTri.setFill('red')
titledownArrowTri.setOutline('red')
titledownArrowLine = Rectangle(Point(453, 143),
                            Point(467, 270))
titledownArrowLine.setFill('red')
titledownArrowLine.setOutline('red')

#main game screen
def main():
    guessCount = 0
    guess = 123
    prevGuess = None
    correct_val = random.randint(1, 20)

    win = GraphWin("Hi or Low Game", 500, 350)
    win.setBackground('black')
    homeScreen(win)

    while guess != correct_val:
        guess = readGuess(win, prevGuess, guessCount)
        guessCount += 1
        if guess < correct_val:
            lower(win, guess, guessCount)
        if guess > correct_val:
            higher(win, guess, guessCount)
        if guess == correct_val:
            correct(win, guess, guessCount)
        prevGuess = guess
        
    win.close()

#reads user input
def readGuess(win, prevGuess, guessCount):
    validGuess = False
    title = Text(Point(250, 50), "Enter a number between 1 and 20.\nOnce it has been entered, double click the window.")
    title.setTextColor('white')
    title.setSize(15)
    title.setFace('helvetica')
    title.draw(win)

    if prevGuess != None:
        prev = Text(Point(150, 100), "Previous Guess: " + str(prevGuess))
        prev.setTextColor('white')
        prev.setSize(12)
        prev.setFace('helvetica')
        prev.draw(win)
    
    count = Text(Point(150, 125), "Guess Count: " + str(guessCount))
    count.setTextColor('white')
    count.setSize(12)
    count.setFace('helvetica')
    count.draw(win)
    
    inputBox = Entry(Point(250, 180), 10)
    inputBox.setFace('helvetica')
    inputBox.setSize(12)
    inputBox.setStyle('bold')
    inputBox.setTextColor('white')
    inputBox.draw(win)
    drawArrows(win)

    while not validGuess:
        guess = inputBox.getText()
        win.getMouse()
        if guess.isnumeric() and 0 < int(guess) < 21:
            validGuess = True
        else:
            warning = Text(Point(250, 200), "WARNING: Enter a numeric guess between 1 and 20.")
            warning.setStyle('bold')
            warning.setTextColor('red')
            warning.setSize(11)
            warning.setFace('helvetica')
            warning.draw(win)
            time.sleep(2)
            warning.undraw()

    clear(win)
    return int(guess)


#home screen
def homeScreen(win):
    titleCard = Rectangle(Point(50, 25), Point(450, 75))
    titleCard.setFill('black')
    titleCard.setOutline('white')
    titleCard.draw(win)

    title = Text(Point(250, 50), "Welcome to the Hi or Low Game!")
    title.setStyle('bold')
    title.setTextColor('white')
    title.setSize(15)
    title.setFace('helvetica')
    title.draw(win)

    instructionCard = Rectangle(Point(80, 130), Point(420, 275))
    instructionCard.setFill('black')
    instructionCard.setOutline('white')
    instructionCard.draw(win)

    
    instructions = Text(Point(250, 200), "The rules are simple:\nEnter a number into the box, and try to\nguess the number from 1-20!\nYour guesses will be counted, so try to\nguess correctly in as few guesses as possible.\nClick the screen to get started.")
    instructions.setTextColor('white')
    instructions.setSize(12)
    instructions.setFace('helvetica')
    instructions.draw(win)
    drawArrows(win)        
    clear(win)

#if the guess is too high
def higher(win, guess, count):
    title = Text(Point(250, 75), "TOO HIGH!\nClick the window to try again.")
    title.setTextColor('white')
    title.setSize(20)
    title.setFace('helvetica')
    title.draw(win)

    regdownArrowLine.draw(win)
    regdownArrowTri.draw(win)

    while win.checkMouse() == None:
        regdownArrowLine.move(0, 5)
        regdownArrowTri.move(0, 5)
        time.sleep(0.5)
        regdownArrowLine.move(0, -5)
        regdownArrowTri.move(0, -5)
        time.sleep(0.5)
    
    clear(win)

#if the guess is too low
def lower(win, guess, guessCount):
    title = Text(Point(250, 75), "TOO LOW!\nClick the window to try again.")
    title.setTextColor('white')
    title.setSize(20)
    title.setFace('helvetica')
    title.draw(win)

    regupArrowLine.draw(win)
    regupArrowTri.draw(win)

    while win.checkMouse() == None:
        regupArrowLine.move(0, -5)
        regupArrowTri.move(0, -5)
        time.sleep(0.5)
        regupArrowLine.move(0, 5)
        regupArrowTri.move(0, 5)
        time.sleep(0.5)

    clear(win)

#if the guess is correct
def correct(win, guess, guessCount):
    win.setBackground(CORRECT_GREEN)
    title = Text(Point(250, 75), "CORRECT! You win.")
    title.setTextColor('white')
    title.setSize(15)
    title.setFace('helvetica')
    title.setStyle('bold')
    title.draw(win)

    checktop.draw(win)
    checkbottom.draw(win)

    while win.checkMouse() == None:
        checktop.move(0, -7)
        checkbottom.move(0, -7)
        time.sleep(0.5)
        checktop.move(0, 7)
        checkbottom.move(0, 7)
        time.sleep(0.5)

    clear(win)

#if the guess is incorrect
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def drawArrows(win):
    titleupArrowTri.draw(win)
    titleupArrowLine.draw(win)

    titledownArrowTri.draw(win)
    titledownArrowLine.draw(win)

    while win.checkMouse() == None:
        titleupArrowTri.move(0, -5)
        titleupArrowLine.move(0, -5)

        titledownArrowTri.move(0, 5)
        titledownArrowLine.move(0, 5)

        time.sleep(0.5)

        titleupArrowTri.move(0, 5)
        titleupArrowLine.move(0, 5)

        titledownArrowTri.move(0, -5)
        titledownArrowLine.move(0, -5)

        time.sleep(0.5)

main()