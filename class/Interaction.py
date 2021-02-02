import datetime
import dill
from random import randint
from Pet import Pet


class Interaction:
    def __init__(self):
        self.pet = None

    def create_pet(self, name: str, species: str, colour: str):
        """"Creates a new Pet object"""
        self.pet = Pet(species, colour, name, datetime.date)

    def feed_pet(self):
        """"hunger+, energy+, clean-"""
        self.pet.update_core("hunger", randint(5, 30))
        self.pet.update_core("energy", randint(5, 40))
        self.pet.update_core("clean", -1)

    def play_pet(self):
        """"energy-, boredom+, clean-"""
        self.pet.update_core("energy", randint(-20, -5))
        self.pet.update_core("boredom", randint(5, 20))
        self.pet.update_core("clean", randint(-15, -5))

    def clean_pet(self):
        """"clean+, boredom=, energy-"""
        self.pet.update_core("clean", 100)
        self.pet.update_core("boredom", randint(-5, 5))
        self.pet.update_core("energy", randint(-5, 0))

    def save_game(self):
        dill.dump(self.pet, file=open("pet.sve", "wb"))

    def load_game(self):
        self.pet = dill.load(open("pet.sve", "rb"))


