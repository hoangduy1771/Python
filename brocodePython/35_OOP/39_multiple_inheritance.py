# multiple inheritance = when a child is derived from more than one parent class

class Prey:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def flee(self):
        print("This " + self.animal_name + " flees")


class Predator:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def hunt(self):
        print("This " + self.animal_name + " hunts")


class Rabbit(Prey):
    def run(self):
        print("This rabbit species: " + self.animal_name + " runs")


class Fish(Prey, Predator):
    def swim(self):
        print("This fish swims")


class Hawk(Predator):
    def fly(self):
        print("This hawk flies")


english_spot_rabbit = Rabbit("English Spot Rabbit")
# salmon_fish = Fish()
# red_tail_hawk = Hawk()

english_spot_rabbit.run()
english_spot_rabbit.flee()



