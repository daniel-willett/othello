#!/usr/bin/python3

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

setup()
display()
