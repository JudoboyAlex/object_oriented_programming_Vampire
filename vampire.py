class Vampire:

    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today
    
    def __repr__(self):
        return "{}".format(self.name)

    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire
    
    def drink_blood(self):
        self.drank_blood_today = True 

    @classmethod
    def sunrise(cls):      
        for vampire in Vampire.coven:
            if vampire.in_coffin == False or vampire.drank_blood_today == False:
                return Vampire.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for self in Vampire.coven:
            self.drank_blood_today = False
            self.in_coffin = False

    def go_home(self):
         self.in_coffin = True
    
vampire1 = Vampire.create("Kawahi", 28, True, True)
vampire2 = Vampire.create("Iverson", 45, False, True)
vampire3 = Vampire.create("Giannis", 21, False, False)
print(len(Vampire.coven))
Vampire.sunset()
print(len(Vampire.coven))
Vampire.sunrise()
print(len(Vampire.coven))
vampire1.go_home()
vampire2.go_home()
print(len(Vampire.coven))
print(Vampire.coven)
