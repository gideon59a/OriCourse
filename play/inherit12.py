# Class 12 - Inheritence

class Animal(object):
    def __init__(self, animal_type, legs, color):
        self.animal_type = animal_type
        self.num_of_legs = legs
        self.skin_color = color

class Cage(Animal):
    def __init__(self, animal_type, legs, color, num_of_animals):
        #print ("is? ",issubclass(Cage, Animal))
        #if python 2.7: super(Animal, self).__init__(animal_type, legs, color)
        super().__init__(animal_type, legs, color)
        self.num_of_animals= num_of_animals

class Zoo:
    def __init__(self):
        self.cages = []  # start with no cages

    def add_cage(self, cage):
        self.cages.append(cage)

    def get_per_legs(self, legs):
        # scan all cages for animals with this numnber of legs
        animals_found = []
        for cage in self.cages:
            if cage.num_of_legs == legs:
                animals_found.append((cage.animal_type, cage.num_of_animals))
        return animals_found

    def get_per_color(self, color):
        # scan all cages for animals with this skin color
        animals_found = []
        for cage in self.cages:
            if cage.skin_color == color:
                animals_found.append((cage.animal_type, cage.num_of_animals))
        return animals_found


myanimal = Animal('Bear', 4, 'brown')

bears_cage = Cage('Bear', 4, 'brown', 20)
snake_cage = Cage('Snake', 0, 'grey', 50)
tiger_cage = Cage('Tiger', 4, 'yellow', 10)

zoo = Zoo()
zoo.add_cage(bears_cage)
zoo.add_cage(snake_cage)
zoo.add_cage(tiger_cage)

animals_found = zoo.get_per_legs(4)
print ("Animals with 4 legs: \n", animals_found)

animals_found = zoo.get_per_color('brown')
print ("Animals with brown color: \n", animals_found)
