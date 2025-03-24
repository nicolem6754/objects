class player:
    def __init__(self,health,gender,name, defualtWeapon, credits):
        print("Player Object Created")
        self.health=health
        self.gender=gender
        self.name=name
        self.defualtWeapon=defualtWeapon
        self.credits=credits

def playerHurt(self,damage):
    self.health=self.health-damage 
    print("Damage=",damage, "New Health=", self.health)

def isDead(self):
    if self.health<=0:
        return True
    else:
        return False  


p1=player(100,"F")
p2=player(90,"M")
print(p1.isDead())
print(p2.isDead())


print(p1.health,p1.gender)
print(p2.health,p2.gender)


