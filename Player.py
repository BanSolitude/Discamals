from random import choice

class Player:
	def __init__(self, Name, Strategy):
		self.name = Name
		self.selectTeam = Strategy
		self.currentTeam = None

	def __unicode__(self):
		return self.name

	def select_team(self, AvailableDiscamals):
		self.currentTeam = self.selectTeam(AvailableDiscamals)

#TODO make these work for teams of arbitrary length
def select_team_randomly(AvailableDiscamals):
	return frozenset([choice(AvailableDiscamals)])

def select_team_manually(PlayersDiscamals):
	_dplayer = ""
	while (not _dplayer in PlayersDiscamals):
		_dplayer = input("Please enter your choice of discamal:").lower()
		if (not _dplayer in PlayersDiscamals):
			print ("Your selection was invalid, please try again")

	return frozenset([_dplayer])