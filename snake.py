from tkinter import * 
from random import randint
from time import sleep

# variables
cols = rows = 8
squareLength = int(1024 / cols)
windowSize = str(cols * squareLength) + "x" + str(rows * squareLength)

# Colours
colourSnake = "#44ff44"
colourBack = "#bbbbcc"
colourFruit = "#ff4444"

# Location Data
fruitLocation = (2, 5)
snakeBody = [[0]*cols for _ in range(rows)]
snakeBody[int(rows/2)][int(cols/2)] = 1
snakeDirection = "N"

# Functions
def validLocation(location):
    if(snakeBody[location[0]][location[1]] == 1):
        return False
    return True

def newFruitLocation():
    # Create location
    location = (randint(0, rows - 1), randint(0, cols - 1))
    while(validLocation(location) == False):
        location = (randint(0, rows - 1), randint(0, cols - 1))
    
    print(location)
    return location

# Setup
root = Tk()

menu = Menu(root) 
root.config(menu=menu)

root.geometry(windowSize) 
root.title('Snake by Dean')

# Menu
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='Start New Game') 
filemenu.add_command(label='Back to Menu') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='Controls') 

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Select Type')

# Game Engine
gameBoard = Canvas(root, bg="white", height=(300), width=(300))

#refresh fruit location
fruitLocation = newFruitLocation()

#draw the board
for row in range(rows):
    for col in range(cols):
        x1 = col * squareLength
        y1 = row * squareLength
        x2 = (col + 1) * squareLength
        y2 = (row + 1) * squareLength
        if(snakeBody[row][col] == 1):
            square = gameBoard.create_rectangle(x1, y1, x2, y2, fill=colourSnake, tags="area")
        elif(row == fruitLocation[1] and col == fruitLocation[0]):
            square = gameBoard.create_rectangle(x1, y1, x2, y2, fill=colourFruit, tags="area")
        else:
            square = gameBoard.create_rectangle(x1, y1, x2, y2, fill=colourBack, tags="area")

#move snake
if(snakeDirection == "N"):

elif(snakeDirection == "E"):

elif(snakeDirection == "S"):

elif(snakeDirection == "W"):

# Pack GameBoard
gameBoard.pack(fill="both", expand="1")

# Loop
root.mainloop()
