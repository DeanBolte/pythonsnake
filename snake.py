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
        self.snakeBody = [[0]*cols for _ in range(rows)] #[[0 <= col, 0, 0] <= row, [0, 0, 0], [0, 0, 0]] [y][x] = [rows][cols]
        self.snakeDirection = "N"

        # Points
        self.points = 0
        self.snakeSize = 3

        # Starting location
        self.snakeBody[int(rows/2)][int(cols/2)] = self.snakeSize
        self.snakeHead = (int(cols/2), int(rows/2))
        self.snakeBodyLocations = [self.snakeHead]

        # Game Board
        self.canvas = Canvas(root, bg="white", height=(300), width=(300))
        self.canvas.pack(fill="both", expand="1")

        # Begins moving the snake
        self.movement() 

    def validLocation(self, location):
        if(location[0] >= cols or location[1] >= rows
        or location[0] < 0 or location[1] < 0):
            # Out of Bounds
            return False
        elif(self.snakeBody[location[1]][location[0]] == 1):
            # Inside Snake
            return False
        # Valid
        return True

    def newFruitLocation(self):
        # Create location
        location = (randint(0, rows - 1), randint(0, cols - 1))
        while(self.validLocation(location) == False):
            location = (randint(0, rows - 1), randint(0, cols - 1))
        
        return location

    def snakeDecay(self):
        for bodyPiece in self.snakeBodyLocations:
            self.snakeBody[bodyPiece[1]][bodyPiece[0]] -= 1
            if(self.snakeBody[bodyPiece[1]][bodyPiece[0]] <= 0):
                self.snakeBodyLocations.remove(bodyPiece)

    def move(self, x, y):
        # Coords to move to
        moveX = self.snakeHead[0] + x
        moveY = self.snakeHead[1] + y

        # If fruit then eat
        if(moveX == self.fruitLocation[0] and moveY == self.fruitLocation[1]):
            self.fruitLocation = self.newFruitLocation()
            self.points += 1
            self.snakeSize += 1

        # Move to coords if valid
        if(self.validLocation((moveX, moveY))):
            #tick down snake body values
            self.snakeDecay()
            #create new head
            self.snakeBody[moveY][moveX] = self.snakeSize
            self.snakeHead = (moveX, moveY)
            self.snakeBodyLocations.append(self.snakeHead)
            print(self.snakeHead)
        else:
            print("cannot move")

    def changeDirection(self, dir):
        self.snakeDirection = dir

    def movement(self):
        #draw the board
        for row in range(rows):
            for col in range(cols):
                x1 = col * squareLength
                y1 = row * squareLength
                x2 = (col + 1) * squareLength
                y2 = (row + 1) * squareLength
                if(self.snakeBody[row][col] >= 1):
                    square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colourSnake, tags="area")
                elif(row == self.fruitLocation[1] and col == self.fruitLocation[0]):
                    square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colourFruit, tags="area")
                else:
                    square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=colourBack, tags="area")

        #move snake
        if(self.snakeDirection == "N"):
            self.move(0, -1)
        elif(self.snakeDirection == "E"):
            self.move(1, 0)
        elif(self.snakeDirection == "S"):
            self.move(0, 1)
        elif(self.snakeDirection == "W"):
            self.move(-1, 0)

        self.canvas.after(400, self.movement)
    
if __name__ == "__main__": 
    gb = GameBoard(root)
  
    # This will bind arrow keys to the tkinter 
    # toplevel which will navigate the image or drawing 
    root.bind("<KeyPress-Left>", lambda e: gb.changeDirection("W")) 
    root.bind("<KeyPress-Right>", lambda e: gb.changeDirection("E")) 
    root.bind("<KeyPress-Up>", lambda e: gb.changeDirection("N")) 
    root.bind("<KeyPress-Down>", lambda e: gb.changeDirection("S")) 
      
    # Infnite loop breaks only by interrupt 
    root.mainloop() 