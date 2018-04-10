from random import choice

class Player:
	def __init__(self, Name, Strategy):
		self.name = Name
		self.selectTeam = Strategy
		self.currentTeam = None

    #TODO is this what I want, or should users have to request name specifically?
	def __str__(self):
		return self.name

	def select_team(self, AvailableDiscamals, TeamSize):
		self.currentTeam = self.selectTeam(AvailableDiscamals, TeamSize)

def select_team_randomly(AvailableDiscamals, TeamSize):
	#Unfortunately we can't use choices here because it chooses with replacement.
	_temp = [disc for disc in AvailableDiscamals]
	_team = []
	while len(_team) < TeamSize:
		_choice = choice(_temp)
		_team.append(_choice)
		_temp.remove(_choice)
	return frozenset(_team)

def select_team_most_wins(AvailableDiscamals, TeamSize):
	_temp = sorted(AvailableDiscamals, key=lambda x: x.tournamentWins, reverse=True)
	return frozenset(_temp[0:TeamSize])

def select_team_manually(PlayersDiscamals, TeamSize):
	_dplayer = None
	_temp = [disc for disc in PlayersDiscamals]
	_team = []
	while len(_team) < TeamSize:
		while (not _dplayer in _temp or _dplayer in _team):
			_name = input("Please enter your choice of discamal:").lower()
			try:
				_dplayer = [disc for disc in PlayersDiscamals if disc.name == _name][0]
			except Exception:
				print ("Your selection was invalid, please try again")
		_team.append(_dplayer)

	return frozenset(_team)
