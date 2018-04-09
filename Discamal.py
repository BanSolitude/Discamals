from random import choice

class Discamal:
    def __init__(self, Name):
        self.name = Name

    #TODO is this what I want, or should users have to request name specifically?
    def __str__(self):
        return self.name

#TODO should more be stored in this class?
#     ie should this hold the created discs, and create potential names
class DiscamalFactory:
    def __init__(self, DiscamalNames):
        self.names = DiscamalNames

    def new_discamal(self):
        _new_name = choice(self.names)
        self.names.remove(_new_name)
        return Discamal(_new_name)
