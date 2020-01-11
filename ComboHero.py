from math import *
from tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=1000, height=800, background="paleturquoise")
screen.pack()

def setInitialValues():
    global energy,score, scoreMultiplier, hit, upImg, downImg, leftImg, rightImg, combo, numZeroes, lives, arrowSpeed, length, speed, level, frame1, frame2, frame3, frame4, frame5, frame6, frame7,skel, knight, plant, moose,newMonster,monstersKilled, monsterHealth

    #initial values
    score = 0
    scoreMultiplier = 1
    energy = 100 #bar ends at y 400
    hit = 700 #where the player hits the key
    combo = 0
    numZeroes = 6
    arrowHit = 0
    length = 8 #starting level is 20 moves
    speed = 17 #speed of arrows coming down
    level = 1
    monsterHealth = 2 #combo you need to kill a monster
    monstersKilled = 0 #num of monsters killed
    
    #arrow images
    upImg = PhotoImage(file = "up.gif")
    downImg = PhotoImage(file = "down.gif")
    leftImg = PhotoImage(file = "left.gif")
    rightImg = PhotoImage(file = "right.gif")
    
    #character Images
    frame1 = PhotoImage(file = "frame1.gif")
    frame2 = PhotoImage(file = "frame2.gif")
    frame3 = PhotoImage(file = "frame3.gif")
    frame4 = PhotoImage(file = "frame4.gif")
    frame5 = PhotoImage(file = "frame5.gif")
    frame6 = PhotoImage(file = "frame6.gif")
    frame7 = PhotoImage(file = "frame7.gif")

    #monster images
    skel = PhotoImage(file = "skel.gif")
    knight = PhotoImage(file = "bloody_knight.gif")
    plant = PhotoImage(file = "plant.gif")
    moose = PhotoImage(file = "moose.gif")
    
def drawObjects():
    global energy, score,scoreboard, comboCount, energyBar, monsterKills,column2,column3,column4,column5,column1,arrow1,arrow2,arrow3,arrow4,charStart, barOutline, hitLine, hitLine2, barLine

    #draw columns that arrows will fall down between
    column1 = screen.create_rectangle(97,0,103,800, fill = "white")
    column2 = screen.create_rectangle(197,0,203,800, fill = "white")

    column3 = screen.create_rectangle(297,0,303,800, fill = "white")
    column4 = screen.create_rectangle(397,0,403,800, fill = "white")

    column5 = screen.create_rectangle(497,0,503,800, fill = "white")
    
    #draw energy bar
    barOutline = screen.create_rectangle(30,99,80,401, fill = "", outline = "white")
    energyBar = screen.create_rectangle(31,400,79,energy, fill = "#F73BF4", outline = "white")
    barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)

    #draw hit line
    hitLine = screen.create_rectangle(97,650,503,655, fill = "white")
    hitLine2 = screen.create_rectangle(97,747,503,753, fill = "white")
    #draw arrows under hit line
    arrow1 = screen.create_image(150,700, image = leftImg)
    arrow2 = screen.create_image(250,700, image = upImg)
    arrow3 = screen.create_image(350,700, image = downImg)
    arrow4 = screen.create_image(450,700, image = rightImg)

    #draw character
    charStart = screen.create_image(650,500, image = frame7)
    #draw score
    scoreboard = screen.create_text(650,100, text = numZeroes*str("0"), font = "Times 35", fill = "#F73BF4")
    
    #draw combo
    comboCount = screen.create_text(650,150, text = str(combo)+"x", font = "Times 35", fill = "#F73BF4")

    #draw monster kill counter
    monsterKills = screen.create_text(750,700, text = "Monsters Killed: " + str(monstersKilled), font = "Times 30", fill = "#F73BF4")
    
def generateMove(): #how it decides what keys show up on screen
    global energy, moves, nextMove, move, secondMove
##    move = [] #array full of moves
          
    moves = ["up","down","left","right"]
  
    move = choice(moves)
    moves.remove(move)
    secondMove = choice(moves)


def characterHit(): #animates character hitting monster if move is hit
    character = [frame1,frame2,frame3,frame4,frame5,frame6,frame7]
    
    if moveHit == True:
        for f in range(len(character)):        
            pic = character[f%len(character)]
            animation = screen.create_image(650,500, image = pic)
            screen.update()
            sleep(0.03)
            screen.delete(animation)
               
def drawMonster(): #draws monster
    global monster, monsters, monsterImg
    
    monsters = [skel, knight, moose, plant]
    monster = choice(monsters)
    monsterImg = screen.create_image(850,500, image = monster)

def drawNewMonster(): #picks a different monster
    global newMonster, monster, monsterImg
    screen.delete(monsterImg)
    newMonster = choice(monsters)

    while newMonster == monster:
        newMonster = choice(monsters)
        
    monster = newMonster
    monsterImg = screen.create_image(850,500, image = monster)

def monsterAlive(): #determines if monster is alive and draws a new one if monster is dead
    
    global monsterHealth, monstersKilled, monsterImg, combo

    if monsterHealth == combo:
        drawNewMonster()
        monsterHealth = monsterHealth + 2
        monstersKilled = monstersKilled + 1
    
def scoreCalculator(): #calculates total score
    global combo, score, secondMoveHit

    bonusPoints = 0 #only above zero if monster is killed
    
    if moveHit == True: #adds one to combo if move is hit
        combo = combo + 1

    if multipleMoveChance%2 == 0:    # if these are two moves checks if second move is hit 
        if secondMoveHit == True:
            combo = combo + 1

        else:
            combo = 0
            
    if moveHit == False: #sets combo to zero if a move is missed
        combo = 0

    if monsterHealth == combo: #adds bonus points for monster kill and draws new monster
        monsterAlive()
        bonusPoints = combo*20
    
    score = score + (10*combo) + bonusPoints

def gameOver(): #when energy is gone starts gameover screen
    global energy, gameRun, scoreboard, comboCount, monsterKills, barOutline, barLine, hitLine, hitLine2, playAgainButton, arrow, PlayAgainButtonPressed, introScreen
   
    if energy == 400:
        screen.delete(scoreboard, comboCount, energyBar, monsterKills,column2,column3,column4,column5,column1,arrow1,arrow2,arrow3,arrow4,charStart, monsterImg, arrow)
        screen.delete(barOutline, barLine, hitLine, hitLine2, comboCount)
        gameRun = "off"
        playAgainButton = Button(root,text = "Play Again?", font = "Times 32", command = PlayAgainButtonPressed) #asks player if they want to play again
        playAgainButton.pack()
        playAgainButton.place(x = 350, y = 250, width = 300, height = 125)
        screen.update()
##        introScreen()
    
def PlayAgainButtonPressed(): #deletes button and runs game again
    global playAgainButton, gameRun, lengthAdd, speedAdd, lives
    playAgainButton.destroy()
    screen.update()
    gameRun = "On"
    runGame()
    
def scoreUpdate(): #updates score and combo in game
    global combo, score, numZeroes, scoreboard, comboCount, monsterKills
    numZeroes = 6
    screen.delete(scoreboard, comboCount, monsterKills)
    scoreStr = str(score)
    numZeroes = numZeroes - len(scoreStr)
    scoreboard = screen.create_text(650,100, text = numZeroes*str("0")+str(score), font = "Times 35", fill = "#F73BF4")
    comboCount = screen.create_text(650,150, text = str(combo)+"x", font = "Times 35", fill = "#F73BF4")
    monsterKills = screen.create_text(750,700, text = "Monsters Killed: " + str(monstersKilled), font = "Times 30", fill = "#F73BF4")
    
def drawMove(): #animates an arrow coming down
    global energy, move, arrowSpeed, arrowY, arrow,nextMove, secondMove, key, moveHit, arrowHit, combo, speed, secondMoveHit, multipleMoveChance, gameRun

    if gameRun == "On":
    
        arrowY = 0 #starting point of each arrow
        generateMove()#generates a  random move
        arrowSpeed = speed #how fast arrows will come down
        multipleMoveChance = randint(1,4) #chance that there will be two moves at once instead of one
        moveHit = False

        if multipleMoveChance%2 == 0:
            secondMoveHit = False
            
        while arrowY <= 880 and moveHit == False: #arrows disappear after they leave the screen and unless the arrow is hit it keeps moving
                            
            if move == "left":
                arrow = screen.create_image(150,arrowY, image = leftImg)
                key = "left"
            elif move == "up":
                arrow = screen.create_image(250,arrowY, image = upImg)
                key = "up"
            elif move == "down":
                arrow = screen.create_image(350,arrowY, image = downImg)
                key = "down"
            elif move == "right":
                arrow = screen.create_image(450,arrowY, image = rightImg)
                key = "right"

            if multipleMoveChance%2 == 0:

                if secondMove == "left":
                    secondArrow = screen.create_image(150,arrowY, image = leftImg)
                    key = "left"
                elif secondMove == "up":
                    secondArrow = screen.create_image(250,arrowY, image = upImg)
                    key = "up"
                elif secondMove == "down":
                    secondArrow = screen.create_image(350,arrowY, image = downImg)
                    key = "down"
                elif secondMove == "right":
                    secondArrow = screen.create_image(450,arrowY, image = rightImg)
                    key = "right"
                    
            arrowY = arrowY + arrowSpeed
            screen.update()
            sleep(0.03)
            screen.delete(arrow)

            if multipleMoveChance%2 == 0:
                screen.delete(secondArrow)
           

        arrowSpeed = 0 #when moveHit is true it stops the arrow
    
    
def calculateDifficulty(): #sets parameters for difficulty
    global length, arrowSpeed, speed, lengthAdd, speedAdd
    length = length + lengthAdd #increase number of moves per speed
    speed = speed + speedAdd
        
def hitDetector(event): #detects keys
    global energy, move, arrowSpeed, arrowY, arrow,nextMove, secondMove, key, hit, moveHit, keyDown
    
    if event.keysym == "Up" :
        if key == "up" and hit-40 < arrowY < hit+40: #if arrow is up and it is in range of the hit line then moveHit is true
             moveHit = True
            
             if multipleMoveChance%2 == 0: #for the second move
                 secondMoveHit = True
        else:
             if arrowY<hit-50 and moveHit == False: 
                energyUpdate() #if key is pressed but arrow is not on hit line energy is lost, prevents spamming of keys, don't lose any energy if keypress was close but didn't hit

    elif event.keysym == "Down":        
        if key == "down" and hit-40 < arrowY < hit+40:
             moveHit = True

             if multipleMoveChance%2 == 0:
                 secondMoveHit = True
        else:

             if arrowY<hit-50 and moveHit == False: 
                energyUpdate()
                   
    elif event.keysym == "Left":
        if key == "left" and hit-40 < arrowY < hit+40:
             moveHit = True

             if multipleMoveChance%2 == 0:
                 secondMoveHit = True
        else:

             if arrowY<hit-50 and moveHit == False: 
                 energyUpdate()
        
    elif event.keysym == "Right":
        if key == "right" and hit-40 < arrowY < hit+40:
             moveHit = True

             if multipleMoveChance%2 == 0:
                 secondMoveHit = True
        else:
             if arrowY<hit-50 and moveHit == False: 
                 energyUpdate()
            
def energyUpdate(): #updates energy bar in game
    global energy, moveHit, energyLoss, oneEnergy, energyGain, miss, energyBar, lives, secondMoveHit
    oneLife = 300/lives
    energyGain = (300/lives)/4

    if moveHit == False: #if false draws an energy bar lower
        if energy+oneLife >= 400:
            energy = 400
            screen.delete(energyBar)
            energyBar = screen.create_rectangle(31,400,79,energy, fill = "#F73BF4", outline = "white")
            barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)

        else:
            screen.delete(energyBar)
            energyBar = screen.create_rectangle(31,400,79,energy+oneLife, fill = "#F73BF4", outline = "white")
            barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)
            energy = energy+oneLife

    
    
    elif moveHit == True: #if true draws energy bar with more energy
        if energy-energyGain <= 100:
            energy == 100
            screen.delete(energyBar)
            energyBar = screen.create_rectangle(31,400,79,energy, fill = "#F73BF4", outline = "white")
            barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)
            
        else:
            screen.delete(energyBar)
            energyBar = screen.create_rectangle(31,400,79,energy-energyGain, fill = "#F73BF4", outline = "white")
            barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)       
            energy = energy-energyGain

    if multipleMoveChance%2 == 0:

        if secondMoveHit == False:
            if energy-energyGain <= 100:
                energy == 100
                screen.delete(energyBar)
                energyBar = screen.create_rectangle(31,400,79,energy, fill = "#F73BF4", outline = "white")
                barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)
                
            else:
                screen.delete(energyBar)
                energyBar = screen.create_rectangle(31,400,79,energy-energyGain, fill = "#F73BF4", outline = "white")
                barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)       
                energy = energy-energyGain

        elif secondMoveHit == True:
            if energy+oneLife >= 400:
                energy = 400
                screen.delete(energyBar)
                energyBar = screen.create_rectangle(31,400,79,energy, fill = "#F73BF4", outline = "white")
                barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)

            else:
                screen.delete(energyBar)
                energyBar = screen.create_rectangle(31,400,79,energy+oneLife, fill = "#F73BF4", outline = "white")
                barLine = screen.create_line(30,250,80,250, fill = "white", width = 2)
                energy = energy+oneLife

    gameOver()

def introScreen():
    global instructionButton, gameRun, easyButton, mediumButton, hardButton, comboHero, comboHero2

    #instructions
    instructionButton = Button(root, text = "Instructions", font = "Times 34", command = instructionButtonPressed)
    instructionButton.pack()
    instructionButton.place( x = 350, y = 400, width=300, height = 100)

    #Difficulty Buttons
    easyButton = Button(root, text = "Easy", font = "Times 25", command = easyButtonPress)
    easyButton.pack()
    easyButton.place(x =150, y =550, width = 150, height = 100)

    mediumButton = Button(root, text = "Medium", font = "Times 25", command = mediumButtonPress)
    mediumButton.pack()
    mediumButton.place(x =425, y =550, width = 150, height = 100)

    hardButton = Button(root, text = "Hard", font = "Times 25", command = hardButtonPress)
    hardButton.pack()
    hardButton.place(x =700, y =550, width = 150, height = 100)

    #title
    comboHero = screen.create_text(500,200, text = "COMBO HERO", font = "Times 60", fill = "red")
    comboHero2 = screen.create_text(505,200, text = "COMBO HERO", font = "Times 61", fill = "yellow")

    screen.update()
def easyButtonPress():
    global lengthAdd, speedAdd, easyButton, mediumButton, hardButton, instructionButton, lives,comboHero, comboHero2, gameRun

    lengthAdd = 10 #after this many arrows speed is updated
    speedAdd = 4 #speed of arrows
    lives = 8
    instructionButton.destroy()
    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()
    screen.delete(comboHero, comboHero2)
    gameRun = "On"

    runGame()
def mediumButtonPress():
    global lengthAdd, speedAdd, easyButton, mediumButton, hardButton, instructionButton, lives,comboHero, comboHero2, gameRun
    lengthAdd = 7
    speedAdd = 5
    lives = 6
    instructionButton.destroy()
    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()
    screen.delete(comboHero, comboHero2)
    gameRun = "On"

    runGame()
def hardButtonPress():
    global lengthAdd, speedAdd, easyButton, mediumButton, hardButton, instructionButton, lives,comboHero, comboHero2, gameRun
    lengthAdd = 5
    speedAdd = 8
    lives = 4
    instructionButton.destroy()
    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()
    screen.delete(comboHero, comboHero2)
    gameRun = "On"
    
    runGame()
def instructionButtonPressed():
    global backButton, instructions, instructions2, objective1, objective2, objective3, objective4, gameRun, easyButton, hardButton, mediumButton
    
    easyButton.destroy()
    hardButton.destroy()
    mediumButton.destroy()
    instructionButton.destroy()
    screen.delete(comboHero, comboHero2)

    instructions = screen.create_text(500,150, text = "Arrow keys - press correct arrow on time to hit", font = "Times 30", fill = "white")
    objective1 = screen.create_text(500,400, text = "Objective - you are a combo hero, your objective is to kill as many monsters as you can", font = "Times 20" , fill = "white")
    objective2 = screen.create_text(500,450, text = "by hitting the correct arrow keys on time with the arrows that appear on screen,", font = "Times 20", fill = "white")
    objective3 = screen.create_text(500,500, text = "you will earn points for hitting and killing monsters,", font = "Times 20", fill = "white")
    objective4 = screen.create_text(500,550, text = "keep up a high combo to earn points faster and kill monsters faster!", font = "Times 20", fill = "white")

    backButton = Button(root, text = "Back", font = "Times 25", command = backButtonPressed)
    backButton.pack()
    backButton.place(x = 400, y = 700, width = 200, height = 100)

    screen.update()

    
def backButtonPressed():
    screen.delete(instructions,objective1, objective2, objective3, objective4)
    backButton.destroy()    
    introScreen()
        
def runGame():
    global arrowY, energy
    setInitialValues()
    drawMonster()
    drawObjects()

    while gameRun == "On":

        for i in range(length):
            drawMove()
            characterHit()
            scoreCalculator()
            scoreUpdate()
            energyUpdate()

        calculateDifficulty()
        
root.after(0, introScreen)
screen.bind( "<Key>", hitDetector )  #detects  key


screen.pack() 
screen.focus_set()

##spacing = 50
##for x in range(0, 1000, spacing): 
##    screen.create_line(x, 25, x, 1000, fill="blue")
##    screen.create_text(x, 5, fill = "white",text=str(x), font="Times 9", anchor = N)
##
##for y in range(0, 1000, spacing):
##    screen.create_line(25, y, 1000, y, fill="blue")
##    screen.create_text(5, y, text=str(y), fill = "white",font="Times 9", anchor = W)

root.mainloop() 
