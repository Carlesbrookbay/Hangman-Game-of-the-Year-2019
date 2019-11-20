import random
import turtle
import math
import time
wordList = ['validate', 'vital', 'stark', 'static', 'scorn', 'quirk', 'paramount', 'potent', 'malleable', \
           'infer', 'impart', 'fiscal', 'evoke', 'entail', 'endure', 'dismay', 'decree', 'conduct', \
           'clout', 'avid']
secretWord = random.choice(wordList)
wrongLetters = []
correctLetters = []
print(wordList)
print(f"the secret word is {secretWord}")

wrongGuesses = 0
MAX_GUESSES = 13
screenWord = ""

topFont = 70

#Setup for screen
sWidth = 1200
sHeight = 600
turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(sWidth, sHeight)
screen.bgcolor(75, 156, 116)

#setup for turtle
t = turtle.getturtle()
t.shape("turtle")
t.color(209, 52, 89)
t.width(5)
t.speed(0)
t.penup()
t.hideturtle()

topScreenTurtle = turtle.Turtle()
topScreenTurtle.shape("turtle")
topScreenTurtle.color(0, 0, 89)
topScreenTurtle.width(5)
topScreenTurtle.speed(0)
topScreenTurtle.penup()
topScreenTurtle.goto(-1 * int(sWidth/2) +int(sWidth * 0.02), -1 * int(sHeight/2) + int(sHeight * .1))
topScreenTurtle.hideturtle()


bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.shape("turtle")
bottomScreenTurtle.color(0, 252, 0)
bottomScreenTurtle.width(5)
bottomScreenTurtle.speed(0)
bottomScreenTurtle.penup()
bottomScreenTurtle.goto(-1 * int(sWidth/2) +int(sWidth * 0.12), -1 * int(sHeight/2) + int(sHeight * 0.25))
bottomScreenTurtle.setheading(0)
bottomScreenTurtle.hideturtle()
#Positions
righthandLoc = (0,0)
lefthandLoc = (0,0)
centerLoc = (0,0)
leftfootLoc = (0,0)
rightfootLoc = (0,0)

def drawGallows():
    t.forward(int(sWidth/8))
    t.right(90)
    t.forward(int(sHeight * .25))
    t.left(90)
    t.pendown()
    t.forward(int(sWidth * 0.3))
    t.backward(int(sWidth * .15))
    t.left(90)
    t.forward(int(sHeight * .66))
    t.left(90)
    t.forward(int(sWidth * .125))
    t.left(90)
    t.forward(int(sHeight * .1))

def drawHead():
    t.right(90)
    t.circle(int(sHeight * .06))
def drawHat():
    t.forward(int(sWidth * .05))
    t.backward(int(sWidth * .025))
    t.right(90)
    t.forward(int(sHeight * .07))
    t.right(90)
    t.forward(int(sWidth * .05))
    t.right(90)
    t.forward(int(sHeight * .07))
    t.left(90)
    t.forward(int(sWidth * .025))
    t.left(180)
    t.forward(int(sWidth * .05))

def drawBody():
    t.left(90)
    t.penup()
    t.forward(int(sHeight * .06) * 2)
    t.pendown()
    t.forward(int(sHeight * .18))
def drawtie():
    t.backward(int(sHeight * .18))
    t.left(15)
    t.forward(int(sHeight * .12))
    t.right(65)
    t.forward(int(sHeight * .04))
    t.right(85)
    t.forward(int(sHeight * .04))
    t.right(62)
    t.forward(int(sHeight * .12))
    t.right(165)
    t.penup()
    t.forward(int(sHeight * .18))
    t.pendown()

def drawrightleg():
    t.left(45)
    t.forward(int(sWidth * .1))
    t.left(180)
    t.forward(int(sWidth * .1))
def drawleftleg():
    t.left(90)
    t.forward(int(sWidth * .1))
    t.left(180)
    t.forward(int(sWidth * .1))
    t.left(45)
    t.forward(int(sHeight * .12))
def drawleftarm():
    t.left(135)
    t.forward(int(sWidth * .075))
    t.backward(int(sWidth * .075))
    t.position = centerLoc
def drawrightarm():
    t.left(90)
    t.forward(int(sWidth * .075))
    t.backward(int(sWidth * .075))
def drawrighteye():
    t.left(135)
    t.penup()
    t.forward(int(sHeight * .13))
    t.left(90)
    t.forward(int(sWidth * .012))
    t.pendown()
    t.circle(int(sHeight * .01))
def drawlefteye():
    t.penup()
    t.backward(int(sHeight * .05))
    t.pendown()
    t.circle(int(sHeight * .01))
    t.penup()
    t.forward(int(sHeight * .03))
    t.left(90)
    t.forward(int(sHeight * .04))
def drawsmile():
    t.left(90)
    t.pendown()
    t.forward(int(sWidth * .02))
    t.backward(int(sWidth * .02))


def drawleftshoe():
    t.penup()
    t.right(90)
    t.forward(int(sHeight * .225))
    t.right(45)
    t.forward(int(sWidth * .09))
    t.pendown()
    t.right(90)
    t.circle(int(sWidth * .02))
    t.left(90)
def drawrightshoe():
    t.penup()
    t.backward(int(sWidth * .09))
    t.left(90)
    t.forward(int(sWidth * .09))
    t.pendown()
    t.right(90)
    t.circle(int(sWidth * .02))
    t.hideturtle()


#drawGallows()
#drawHead()
#drawBody()
#drawrightleg()
#drawleftleg()
#drawleftarm()
#drawrightarm()
#drawrighteye()
#drawlefteye()
#drawsmile()
#drawleftshoe()
#drawrightshoe()


def updatedrawing():
    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawHat()
    if wrongGuesses == 3:
        drawBody()
    if wrongGuesses == 4:
        drawtie()
    if wrongGuesses == 5:
        drawrightleg()
    if wrongGuesses == 6:
        drawleftleg()
    if wrongGuesses == 7:
        drawleftarm()
    if wrongGuesses == 8:
        drawrightarm()
    if wrongGuesses == 9:
        drawrighteye()
    if wrongGuesses == 10:
        drawlefteye()
    if wrongGuesses == 11:
        drawsmile()
    if wrongGuesses == 12:
        drawleftshoe()
    if wrongGuesses == 13:
        drawrightshoe()

def drawWrongLetters():
    topScreenTurtle.clear()
    letterString = "Wrong Letters: "
    for l in wrongLetters:
        letterString += l + ", "
    letterString = letterString[0: len(letterString)-2]
    topScreenTurtle.write(letterString, move=False, align="left", font=("Arial", topFont, "normal"))


def drawWord():
    global screenWord
    # step 1 save turtle info
    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomScreenTurtle.clear()
    bottomScreenTurtle.penup()
    bottomScreenTurtle.goto(-1 * int(sWidth/2) +int(sWidth * 0.12), -1 * int(sHeight/2) + int(sHeight * 0.25))
    bottomScreenTurtle.hideturtle()
    bottomScreenTurtle.setheading(0)

    screenWord = ""


    for letter in secretWord:
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "
    bottomScreenTurtle.write(screenWord, move=False, align="left", font=("Arial", 75, "normal"))
    #t.goto(tLoc)
    #t.setheading(currentHead)
    t.hideturtle()
print (secretWord)




def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + ", "



    boxTitle = "Letters Used:" + badLetterString

    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word")
    return theGuess

def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align="left", font=("Arial", topFont, "normal"))
    time.sleep(2)
    topScreenTurtle.clear()
    topScreenTurtle.hideturtle()


def printWinOrLose(win):
    global screenWord
    topScreenTurtle.clear()
    if win:
        screenWord = secretWord
        drawWord()
        topScreenTurtle.write("You Win!!!", move=False, align="left", font=("Arial", topFont, "normal"))
    else:
        topScreenTurtle.write("I'm sorry. Game over...", move=False, align="left", font=("Arial", topFont, "normal"))



def getWordGuess():
    playerWordGuess = screen.textinput("Guess it", "Enter your guess of the word")

    if playerWordGuess.lower() == secretWord:
        #celebrate win
        printWinOrLose(True)
        return False
    else:
        #celebrate failure
        printWinOrLose(False)
        time.sleep(1)
        writeErrorMessage("The secret word is: " + secretWord)
        return False

gameOn = True
updatedrawing()
#main game
while gameOn:
    drawWord()


    guess = str(getGuess())


    if guess == "$$":
           gameOn = getWordGuess()
    elif len(guess) != 1:
        writeErrorMessage("I need a single letter. Guess Again")
        drawWrongLetters()
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("You need to use letters dummy")
    elif guess.lower() in  wrongLetters:
        writeErrorMessage("You already guessed "+ guess + ", Guess Again")
        drawWrongLetters()
    elif guess.lower() in correctLetters:
        writeErrorMessage(guess + " is in the word. Guess Again")
        drawWrongLetters()
    else:
        if guess.lower() in secretWord.lower():
            correctLetters.append(guess.lower())
            drawWord()
        else:
            #wrong the letter is wrong
            wrongLetters.append(guess.lower())
            wrongGuesses += 1
            drawWrongLetters()
            updatedrawing()

        if(wrongGuesses >= MAX_GUESSES):
            writeErrorMessage("You are out of guesses. Game over.")
            gameOn = False
            writeErrorMessage("The secret word is: " + secretWord)

        if "_" not in screenWord:
            drawWord()
            writeErrorMessage("Congrats you Win!!")
            gameOn = False



    #get a guess
    #check the guess

    #if guest is letter
    #check the lette
    #tell them whether its wrong
    #if wrong show it on screen
    #if it is wrong take away a chance
    #if wrong add a body part
    #if it is write show the letter
    #if wrong and out of chances stop the game

    #if they guess the word --done
    #they win --done
    #they lose





turtle.mainloop()