from being import *
from functions import *
from random import *

human = Human("Protag",40,False,'Human')
ZB = ZomBoss()

human.givestats()
ZB.givestats()
f = open('Map.txt','r')
MAP =[]
string = f.readline()
c = 0
while string !="":
    l = string.split()
    MAP.append(l)
    c += 1
    string = f.readline()

MAP.pop()

row = len(MAP)
col = len(MAP[0])



human.givestats()
pos = [3,3]
print("You wake up in a field with a machete, an empty gun and a single bandage. You're at position",pos[0],pos[1],".\n")


print(pos)
print(pos[0],pos[1])

key = 0
i = 0
goal = 2
print("The map is a 7x7 grid. You are in the center (pos 3,3). You can go north, south, east or west.")
print("Simply type the starting letter of the cardinal direction. and you will move one space that way.")

while key < goal:
    CP = tuple(pos)
    if i < 1:
        i = 1
        print(end="Move around. Input !move for movement commands. Input !stat to see your stats. Input !fight for fight commands.\n\n")
    inp = input("Input:")
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
        print("You are at position",pos[0],pos[1],".")

    elif inp == 'E' or inp == 'e':
        temp = pos[1]
        pos[1] += 1
        if pos[1] < 0 or pos[1] > col-1:
            print("You've hit a wall. You go nowhere.")
            pos[1] = temp
        print("You are at position",pos[0],pos[1],".")

    elif inp == 'S' or inp == 's':
        temp = pos[0]
        pos[0] += 1
        if pos[0] < 0 or pos[0] > row-1:
            print("You've hit a wall. You go nowhere.")
            pos[0] = temp
        print("You are at position",pos[0],pos[1],".")

    elif inp == 'N' or inp == 'n':
        temp = pos[0]
        pos[0] -= 1
        if pos[0] < 0 or pos[0] > row-1:
            print("You've hit a wall. You go nowhere.")
            pos[0] = temp
        print("You are at position",pos[0],pos[1],".")

    status = getprop(pos[0],pos[1],MAP,human)
    if not status:
        break

    key = human.getkey()

    

    



if key == goal:
    print("Congratulations! You got the keys you needed and you make your way out of the decrepit asylum!")    
