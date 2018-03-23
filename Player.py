from random import choice

class Player:
	def __init__(self, Name, Strategy):
		self.name = Name
		self.selectDisc = Strategy
		self.currentDisc = None

	def __unicode__(self):
		return self.name

	def select_disc(self, AvailableDiscamals):
		self.currentDisc = self.selectDisc(AvailableDiscamals)

def select_disc_randomly(AvailableDiscamals):
	return choice(AvailableDiscamals)

def select_disc_manually(PlayersDiscamals):
	_dplayer = ""
	while (not _dplayer in PlayersDiscamals):
		_dplayer = input("Please enter your choice of discamal:").lower()
		if (not _dplayer in PlayersDiscamals):
			print ("Your selection was invalid, please try again")

	return _dplayer