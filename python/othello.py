#!/usr/bin/python3
import re

def setup():
    for i in range(8):
        temp = []
        for j in range(8):
            temp.append(0)
        grid.append(temp)
    grid[3][3] = 1
    grid[4][4] = 1
    grid[3][4] = 2
    grid[4][3] = 2

def display():
    for i in range(8):
        print(str(8-i)+" "+str(grid[i]))
    print("   A  B  C  D  E  F  G  H") 

def interpretInput(usrInput):
    lookup = {"A":0,
              "B":1,
              "C":2,
              "D":3,
              "E":4,
              "F":5,
              "G":6,
              "H":7}
    usrInput = usrInput.replace(" ","")
    match = re.search("^[A-H][,-;:_]*[1-8]$", usrInput)
    if match==None:
        return -1
    char = (re.search("[A-H]",usrInput)).group()
    x = lookup[char]
    y = int((re.search("[1-8]", usrInput)).group())-1 #Arrays start at 0
    y = 7-y #The display is in reverse order to the `grid` indexing
    return [x,y]

def makeMove(position):
    global player
    x = position[0]
    y = position[1]
    if grid[y][x]!=0:
        print("This position is already taken. Please choose an empty position")
        player -= 1 #The next step is to increment it to the next player but we want the current player to try again
    else:
        if isLegal(x,y,player)==False:
            print("This is not a legal play")
            player -= 1 #Same reason as a couple lines before
        else:
            #grid[y][x]=player
            #Also need something else like an actual move being 'played' so perhaps just combine? That's a future problem. For now we work on `isLegal`

def isLegal(x,y,player):
    #We're going to check N, NE, E, SE, S, SW, W, NW
    opponent = (player%2)+1

#Initialise
grid = []
"""
8 [0, 0, 0, 0, 0, 0, 0, 0]
7 [0, 0, 0, 0, 0, 0, 0, 0]
6 [0, 0, 0, 0, 0, 0, 0, 0]
5 [0, 0, 0, 1, 2, 0, 0, 0]
4 [0, 0, 0, 2, 1, 0, 0, 0]
3 [0, 0, 0, 0, 0, 0, 0, 0]
2 [0, 0, 0, 0, 0, 0, 0, 0]
1 [0, 0, 0, 0, 0, 0, 0, 0]
   A  B  C  D  E  F  G  H
"""
gameOver = False
player = 1


setup()
while gameOver==False:
    display()
    print("Player "+str(player)+"'s turn:")
    usrInput = input("where would you like to place?\n")
    position = interpretInput(usrInput)
    if position==-1:
        print("======Invalid input======")
    else:
        makeMove(position)
        player = (player%2)+1 #Switch between (0,1) but scaled by 1 so switch between (1,2)
