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

class GameBoard:
    def __init__(self, root = None): 
        self.root = root 

        # Location Data
        self.fruitLocation = (2, 5)
        self.snakeBody = [[0]*cols for _ in range(rows)]
        self.snakeDirection = "N"

        # Starting location
        self.snakeBody[int(rows/2)][int(cols/2)] = 1
        self.snakeHead = (int(rows/2), int(cols/2))

        # Game Board
        self.canvas = Canvas(root, bg="white", height=(300), width=(300))
        self.canvas.pack(fill="both", expand="1")

        # Begins moving the snake
        self.movement() 

    def validLocation(location):
        if(self.snakeBody[location[0]][location[1]] == 1):
            return False
        elif(location[0] >= rows or location[1] >= cols):
            return False
        return True

    def newFruitLocation():
        # Create location
        location = (randint(0, rows - 1), randint(0, cols - 1))
        while(validLocation(location) == False):
            location = (randint(0, rows - 1), randint(0, cols - 1))
        
        print(location)
        return location

    def move(x, y):
        if(self.validLocation((self.snakeHead[0] + x, self.snakeHead[1] + y))):
            self.snakeBody[self.snakeHead[0] + x][self.snakeHead[1] + y] = 1

    def changeDirection(dir):
        self.snakeDirection = dir

    def movement():
        #refresh fruit location
        self.fruitLocation = self.newFruitLocation()

        #draw the board
        for row in range(rows):
            for col in range(cols):
                x1 = col * squareLength
                y1 = row * squareLength
                x2 = (col + 1) * squareLength
                y2 = (row + 1) * squareLength
                if(self.snakeBody[row][col] == 1):
                    square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colourSnake, tags="area")
                elif(row == self.fruitLocation[1] and col == self.fruitLocation[0]):
                    square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colourFruit, tags="area")
                else:
                    square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colourBack, tags="area")

        #move snake
        if(self.snakeDirection == "N"):
            move(0, -1)
        elif(self.snakeDirection == "E"):
            move(1, 0)
        elif(self.snakeDirection == "S"):
            move(0, 1)
        elif(self.snakeDirection == "W"):
            move(-1, 0)

        self.canvas.after(1000, movement)
    
if __name__ == "__main__": 
    # object of class Tk, resposible for creating 
    # a tkinter toplevel window  
    gb = GameBoard(root)
  
    # This will bind arrow keys to the tkinter 
    # toplevel which will navigate the image or drawing 
    root.bind("<KeyPress-Left>", lambda e: gb.changeDirection("W")) 
    root.bind("<KeyPress-Right>", lambda e: gb.changeDirection("E")) 
    root.bind("<KeyPress-Up>", lambda e: gb.changeDirection("N")) 
    root.bind("<KeyPress-Down>", lambda e: gb.changeDirection("S")) 
      
    # Infnite loop breaks only by interrupt 
    root.mainloop() 