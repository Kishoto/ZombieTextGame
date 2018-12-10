from being import *
from functions import *
from random import *

def Zombies():


    human = Human("Protag",40,False,'Human')
    human.givestats()


    tiles = {'ZB': 0.04,'zom': 0.2,'HP': 0.06,'WP': 0.08}
    tilenum = tiles

    #length = int(input("Enter the length (east to west distance) you want the map to be:"))
    #width = int(input("Enter the width (north to south distance) you want the map to be:"))
    length = 10
    width = 8
    totsq = length*width

    for i in tiles:
        tilenum[i] = int(tilenum[i]*totsq)

    emptytiles = totsq - sum(tilenum.values())
    tilenum['null'] = emptytiles
    chooser = list(tiles.keys())

    MAP2 = []
    ml  = [0]*width

    for i in range(length):
        MAP2.append(ml)
    print(MAP2)
    print()
    MAP2[3][3] = 'hey'
    print(MAP2)
    #This loop makes all of MAP2 null. WTF.
    for i in range(length):
        print(i)
        for j in range(width):
            x = choice(chooser)
            MAP2[i][j] = x
            tilenum[x] -= 1
            if tilenum[x] == 0:
                chooser.remove(x)
    print(MAP2)
    print("\n\n")
    
    for i in range(length):
        shuffle(MAP2[i])
        print(MAP2[i])
        
    
    
    f = open('Map.txt','r')
    MAP =[]
    string = f.readline()
    c = 0
    while string !="":
        l = string.split()
        MAP.append(l)
        c += 1
        string = f.readline()

    row = len(MAP)
    col = len(MAP[0])
    pos = [3,3]
    print("You wake up alone in the dark with a machete, an empty gun and a single bandage. You look around and spy a map on the wall. It tells you that you are currently at position [",pos[0],",",pos[1],"].")
    print("You can see from the map that you are at the center of a %d by %d grid." % (row,col))
    print("You can hear groaning in the distance and the hallways are dimly lit and narrow, meaning you have no idea what awaits you down them. One thing is certain however; you gain nothing my staying here. You must escape.\n")
    key = 0
    i = 0
    goal = 2

    while key < goal:
        CP = tuple(pos)
        if i < 1:
            i = 1
            print(end="Navigate the decrepit asylum. Type !help for a list of useful commands you can input.\n\n")
        inp = input("Input:")

        if inp == '!help':
            print("Enter !move for a list of movement commands. Input !stat to see your current stats. Input !fight for fight commands.")
            continue
                  
        if inp == '!move':
            print("Type N to go north, S to go south and so on.")
            continue

        if inp == '!stat':
            human.givestats()
            continue

        if inp == '!fight':
            print("In a fight, type A to attack with your machete, S to shoot your gun (this uses up bullets!), H to heal (this uses up bandages) and R to attempt to run away (there's a 2/3 chance you get away).")
            continue

        if inp == 'W' or inp == 'w':
            temp = pos[1]
            pos[1] -= 1
            if pos[1] < 0 or pos[1] > col-1:
                print("You've hit a wall. You go nowhere.")
                pos[1] = temp
            print("You are at position [",pos[0],",",pos[1],"]")

        elif inp == 'E' or inp == 'e':
            temp = pos[1]
            pos[1] += 1
            if pos[1] < 0 or pos[1] > col-1:
                print("You've hit a wall. You go nowhere.")
                pos[1] = temp
            print("You are at position [",pos[0],",",pos[1],"]")

        elif inp == 'S' or inp == 's':
            temp = pos[0]
            pos[0] += 1
            if pos[0] < 0 or pos[0] > row-1:
                print("You've hit a wall. You go nowhere.")
                pos[0] = temp
            print("You are at position [",pos[0],",",pos[1],"]")

        elif inp == 'N' or inp == 'n':
            temp = pos[0]
            pos[0] -= 1
            if pos[0] < 0 or pos[0] > row-1:
                print("You've hit a wall. You go nowhere.")
                pos[0] = temp
            print("You are at position [",pos[0],",",pos[1],"]")
        else:
            print("Please enter a valid command")
            continue


        status = getprop(pos[0],pos[1],MAP,human)
        if not status:
            break

        key = human.getkey()

        

        



    if key == goal:
        print("Congratulations! You got the keys you needed and you make your way out of the decrepit asylum!")    

def main():
    Zombies()

main()
