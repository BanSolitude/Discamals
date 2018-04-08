from random import choice

class Player:
	def __init__(self, Name, Strategy):
		self.name = Name
		self.selectTeam = Strategy
		self.currentTeam = None

	def __unicode__(self):
		return self.name

	def select_team(self, AvailableDiscamals, TeamSize):
		self.currentTeam = self.selectTeam(AvailableDiscamals, TeamSize)

def select_team_randomly(AvailableDiscamals, TeamSize):
	#Unfortunately we can't use choices here because it chooses with replacement.
	_temp = [disc for disc in AvailableDiscamals]
	_team = []
	while len(_team) < TeamSize:
		_team.append(choice(AvailableDiscamals))
	return frozenset(_team)

def select_team_manually(PlayersDiscamals, TeamSize):
	_dplayer = ""
	_temp = [disc for disc in PlayersDiscamals]
	_team = []
	while len(_team) < TeamSize:
		while (not _dplayer in _temp or _dplayer in _team):
			_dplayer = input("Please enter your choice of discamal:").lower()
			if (not _dplayer in _temp or _dplayer in _team):
				print ("Your selection was invalid, please try again")
		_team.append(_dplayer)

	return frozenset(_team)