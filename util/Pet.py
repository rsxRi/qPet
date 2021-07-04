import datetime


class Pet:
    def __init__(self, species: str,
                 colour: str,
                 name: str,
                 birthday=datetime.date,
                 age: int = 0,
                 health: int = 100, energy: int = 100, boredom: int = 50, clean: int = 100, hunger: int = 50):
        self.species = species
        self.colour = colour
        self.birthday = birthday
        self.name = name
        self.age = age
        # Lower core value is worse than high core value
        self.cores = {"health": health,
                      "energy": energy,
                      "boredom": boredom,
                      "clean": clean,
                      "hunger": hunger}

    def update_age(self, val: int):
        """Updates the age attribute"""
        self.age += val

    def update_core(self, core: str, val: int):
        """Update a core attribute value"""
        self.cores[core] += val

        if self.cores[core] > 100:
            self.cores[core] = 100
        elif self.cores[core] < 0:
            self.cores[core] = 0

        if self.cores["health"] <= 0:
            self.death()

    def change_name(self, name):
        """Changes the pet's name"""
        self.name = name

    def death(self):
        return f'{self.name} has passed on.\n' \
               f'{self.name} was a {self.colour} {self.species} and was {self.age} days old.'

    def __str__(self):
        return_string = f"{self.name}\n{self.species}\n{self.colour}\n"
        for i in self.cores:
            return_string += f"{self.cores[i]}\n"
        return return_string
