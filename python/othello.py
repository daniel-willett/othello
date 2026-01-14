#!/usr/bin/python3
import re

grid = []

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
    usrInput = usrInput.replace(" ","")
    match = re.search("^[A-H][,-;:_]*[1-8]$", usrInput)
    if match==None:
        return -1
    char = (re.search("[A-H]",usrInput)).group()
    num = (re.search("[1-8]", usrInput)).group()
    return [char,num]

setup()
gameOver = False
player = 1
while gameOver==False:
    display()
    usrInput = input("where would you like to place?\n")
    position = interpretInput(usrInput)
    if position==-1:
        print("======Invalid input======")
        continue
