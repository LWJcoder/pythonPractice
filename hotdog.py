#coding :utf-8

class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.cndiments = []

    def cook(self, time ):
        self.cooked_level = self.cooked_level+ time
        if self.cooked_level > 8 :
            self.cooked_string = "Charcoal" #½¹ÁË
        elif self.cooked_level >5 :
            self.cooked_string = "well-done"
        elif self.cooked_level >3 :
            self.cooked_string = "medium"
        else:
            self.cooked_string = "Raw"

myDog = HotDog()
myDog.cook(10)
print myDog.cooked_string
