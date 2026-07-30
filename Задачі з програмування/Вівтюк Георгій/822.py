class Animal:
    def __init__(self, species):
        self.species = species
    def show_species(self):
        print(f"I'm an - {self.species}")
    def make_sound(self):
        print("Grrr!")
class Dog(Animal):
    def __init__(self):
        super().__init__("dog")
    def make_sound(self):
        print("Woof! Woof!")
class Cat(Animal):
    def __init__(self):
        super().__init__("cat")
    def make_sound(self):
        print("Meow!")
def show_animal_info(obj):
    if isinstance(obj, Animal):
        obj.show_species()
        obj.make_sound()
    else:
        print(f"{obj} this is not an animal!")
animal = Animal("ordinary animal")
dog = Dog()
cat = Cat()
show_animal_info(animal)
show_animal_info(dog)
show_animal_info(cat)
show_animal_info("Book")