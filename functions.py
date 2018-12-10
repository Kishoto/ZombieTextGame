from being import *
from random import *

def fighting(hum,zom):
    i = 0
    while hum.getHP() > 0 and zom.getHP() > 0:
        if i == 0:
            i = 1
            print(end="You're being attacked by ")
            print(end=zom.getname())
            print(end='! ')
        print(end="What do you do:")
        dec = input()
        if dec == 'A' or dec == 'a':
            hit = randint(hum.getatk()-3,hum.getatk())
            zom.hurt(hit)
            if zom.getHP()<=0:
                return 'win'
            dmg = randint(zom.getatk()-5,zom.getatk())
            hum.hurt(dmg)
        elif dec == 'S' or dec =='s':
            if hum.getbull() >= 1:
                hum.losebull()
                hit = randint(10,20)
                zom.hurt(hit)
                if zom.getHP()<=0:
                    return 'win'
                dmg = randint(zom.getatk()-5,zom.getatk())
                hum.hurt(dmg)
            else:
                print("You have no bullets! The zombie claws you as you fumble with your empty clip.")
                dmg = randint(zom.getatk()-5,zom.getatk())
                hum.hurt(dmg)
            if zom.getHP()<=0:
                return 'win'



        elif dec == 'R' or dec =='r':
            odds = randint(1,3)
            print("You try to run away....")
            if odds > 1:
                return 'run'
            else:
                print("You fail! The zombie mauls you, throwing you to the floor and doing extra damage!")
                dmg = randint(zom.getatk()-3,zom.getatk()+2)
                hum.hurt(dmg)
        elif dec == '!info':
            print()
            zom.givestats()
            print()
            hum.givestats()

        elif dec == 'H' or dec == 'h' or dec == 'B' or dec == 'b':
            if hum.getban() >= 1:
                print("You tie a bandage around your injuries, patching yourself up and healing to full HP.")
                hum.fillHP()
                hum.loseban()
                dmg = randint(zom.getatk()-5,zom.getatk())
                hum.hurt(dmg)
            else:
                print("You have no bandages! The zombie swipes at you as you desperately go through your pockets.")
                dmg = randint(zom.getatk()-5,zom.getatk())
                hum.hurt(dmg)
            if zom.getHP()<=0:
                return 'win'


        else:
            print("Enter a valid fight command! A(ttack), H(eal)/B(andage), S(hoot) or R(un)! You can also type !info to check both your stats and  the enemy's stats!")

        if hum.getHP() <= 0:
            return 'loss'




def getprop(x,y,MAP,hum):
    pos = MAP[x][y]
    res=''
    alive = True
    zomnames1 = ['Moaning ', 'Decapitated ', 'Groaning ', 'Smelly ', 'Slobbery ']
    zomnames2 = ['Tom', 'Bill', 'Alice', 'Brent', 'Nick', 'Steve', 'Rick', 'Jennifer', 'Bob' ]
    zomnames3 = ['Hulking Horror','Massive Malady','Titanic Terror','Spectacular Skeleton']
    zomnames12 = choice(zomnames1) + choice(zomnames2)

    if pos == 'ZB':
        print("A huge lumbering mass of rotten flash lunges for you. A zomboss is attacking you!!")
        res = fighting(hum,ZomBoss(choice(zomnames3)))
    elif pos == 'HP':
        print("You found medical supplies.")
        hum.fillHP()
        hum.addband()
        MAP[x][y] = 'null'
    elif pos == 'WP':
        print("You found a weapons cache!")
        hum.fillHP()
        hum.addband()
        hum.addbull()
        MAP[x][y] = 'null'
    elif pos == 'zom':
        print("From the darkness, you hear a horrifying sound. A zombie leaps out to attack you!")
        res = fighting(hum,Zombie(zomnames12))

    elif pos == 'Start':
        print("You're back where you started.")
        hum.fillHP()
    else:
        print("Nothing's here.")

    if res == 'win':
        print("You beat the enemy!\n")
        if MAP[x][y] == 'ZB':
            hum.givekey()
            print("The zomboss dropped a golden key! You pocket it.\n")

    elif res == 'loss':
        alive = False
        print("You died.\n")

    elif res == 'run':
        print("You got away safely...this time.\n")

    if MAP[x][y] != 'Start' and res != 'run':
        MAP[x][y] = 'null'

    return alive




