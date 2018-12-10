class Being:
    def __init__(self, name="",HP=10,bit=True,TYPE='',atk = 0):
        self._name = name
        self._bit = bit
        self._TYPE = TYPE
        self._HP = HP
        self._atk = atk

    def givestats(self):
        print("Name:",self._name)
        print("HP:",self._HP)
        print("Type:",self._TYPE)
        print("Atk:",self._atk)

    def getHP(self):
        return self._HP

    def getname(self):
        return self._name

    def getatk(self):
        return self._atk

    def hurt(self,num):
        self._HP -= num
        if num >=0:
            print(self._name,"took",num,"damage! Their HP is now",max(self._HP,0))

class Human(Being):
    def __init__(self,name="Protag",HP=40,bit=False,TYPE='',atk = 5,bull=0,ban=1,key = 0):
        super().__init__(name,HP,bit,TYPE,atk)
        self._Type = 'Human'
        self._bull = bull
        self._ban = ban
        self._key = key



    def addband(self):
        self._ban += 1

    def addbull(self):
        self._bull += 3

    def getbull(self):
        return self._bull

    def losebull(self):
        self._bull -= 1

    def getban(self):
        return self._ban

    def loseban(self):
        self._ban -= 1

    def getkey(self):
        return self._key

    def givekey(self):
        self._key += 1

    def fillHP(self):
        self._HP = 40

    def givestats(self):
        print("Name:",self._name)
        print("HP:",self._HP)
        print("Bullets:",self._bull)
        print("Bandages:",self._ban)
        print("Type:",self._TYPE)
        print("Attack:",self._atk)
        print()


class Zombie(Being):
    def __init__(self, name="Zombie",HP=10,bit=True,TYPE='Zombie',atk = 10):
        super().__init__(name,HP,bit,TYPE,atk)


class ZomBoss(Being):
    def __init__(self, name="Z0mb055!!",HP=50,bit=True,TYPE='Boss',atk = 13,key = 1):
        super().__init__(name,HP,bit,TYPE,atk)
        self._key = key


