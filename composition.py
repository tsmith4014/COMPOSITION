# # class Sandwich:
# def __init__(self, bread, filling):
#     self.bread = bread
#     self.filling = filling

# # class PeanutButterAndJelly(Sandwich):

class Filling:
    def __init__(self, type):
        self.type = type


class Bread:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return self.type


class Sandwich:
    def __init__(self, bread, filling):
        self.bread_obj = bread
        self.filling_obj_list = [filling]

    def add_filling(self, filling):
        self.filling_obj_list.append(filling)

    def __str__(self):
        fillings = ""
        for filling in self.filling_obj_list:
            fillings += filling.type + ", "
        return f"I am a sandwich on {self.bread_obj} with {fillings}"


sand_bread = Bread("rye")
pastrami_filling = Filling('pastrami')
saur_filling = Filling("sauerkraut")
dressing_filling = Filling("thousand isalnd")


#sand_filling = Filling("pastrami, kraut, and thousand island")
my_ruben = Sandwich(sand_bread, pastrami_filling)
my_ruben.add_filling(saur_filling)
my_ruben.add_filling(dressing_filling)
print(my_ruben)
