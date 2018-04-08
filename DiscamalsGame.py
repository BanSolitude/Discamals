from random import choice
from Player import *

FREE_ANIMAL_NAMES = ["bear", "chickadee", "cougar", "coyote", "crow", "duck", "goose", "lynx", "orca", "raccoon", "raven", "seagull", "squirrel" ]
USED_ANIMAL_NAMES = []
WINNER = {}

def add_disc(FreeAnimalNames, UsedAnimalNames):
	if ( len(FreeAnimalNames) == 0 ):
		return

	new_animal = choice(FreeAnimalNames)
	FreeAnimalNames.remove(new_animal)
	UsedAnimalNames.append(new_animal)
	return new_animal

#Teams are frozensets.
def get_winner(Team1, Team2, WinnerList):
	#TODO is a case for a "bye" needed here?
	if len(Team1) != len(Team2) or Team1 == Team2:
		return None

	if  ( not (frozenset([Team1,Team2]) in WinnerList) ):
		if (len(Team1) == 1):
			WinnerList[frozenset([Team1,Team2])] = choice([Team1,Team2])

		else:
			_score1 = 0
			_score2 = 0
			for (_disc1, _disc2) in [(x,y) for x in Team1 for y in Team2]:
				if ( _disc1 == _disc2 ):
					continue
				elif ( get_winner( [_disc1], [_disc2], WinnerList ) == frozenset([_disc1]) ):
					_score1 += 1
				else:
					_score2 += 1

			WinnerList[frozenset([Team1,Team2])] = choice([Team1,Team2], [_score1, _score2])


	return WinnerList[frozenset([Team1,Team2])]

#TODO parse input in a better way
#TODO print messages out in a way that's easier to read
def test(PlayersDiscamals, WinnerList):
	print ("Choose two Discamals to discover the winner.")

	print ("First Discamal")
	_d1 = select_team_manually(PlayersDiscamals)
	print ("Second Discamal")
	_d2 = select_team_manually([d for d in PlayersDiscamals if d!=_d1])

	print("%s wins the test." % format_team(get_winner(_d1, _d2, WinnerList)))

	print("")

#TODO make tournaments team rather than just 1v1s
#TODO add ai that choose teams smarter (right now just random)
#TODO make tournaments more than just a single match
def tournament(AvailableDiscamals, Players, WinnerList):
	print("Choose a Discamal to take to the tournament.")
	for player in Players:
		player.select_team(AvailableDiscamals)

	#this is just a work around until tounament code is improved.
	#for now single elim. plan is swiss to top x (8?)
	single_elim(Players, WinnerList)

	print("")

def single_elim(Players, WinnerList):
	_cur_round = [player for player in Players]
	while len(_cur_round) > 1:
		_temp = _cur_round
		_next_round = []
		while len(_temp) > 0:
			_p1 = _temp.pop()
			_p2 = _temp.pop()
			_do_print = _p1.selectTeam == select_team_manually or _p2.selectTeam == select_team_manually
			if _do_print:
				print ("%s selected %s facing %s with %s." % (_p1.name, format_team(_p1.currentTeam), _p2.name, format_team(_p2.currentTeam)))
			_winner = None
			if (_p1.currentTeam == _p2.currentTeam):
				_winner = choice([_p1, _p2])
			else:
				_winning_team = get_winner(_p1.currentTeam, _p2.currentTeam, WinnerList)
				if (_winning_team == _p1.currentTeam):
					_winner = _p1
				else:
					_winner = _p2
			if _do_print:
				print ("%s wins!" % _winner.name)
			_next_round.append(_winner)

		_cur_round = _next_round

	print ("%s won the tournament with %s." % (_cur_round[0].name, format_team(_cur_round[0].currentTeam)))

def format_team(Team):
	return ' '.join(Team)

#TODO Some sort of economy
#TODO Different number of tests/tournaments as the number of discamals goes up.
if __name__ == '__main__':
	_players = [Player(input("Please enter your name:"), select_team_manually), Player("Randy", select_team_randomly), Player("Andy", select_team_randomly), Player("Mandy", select_team_randomly)]

	print ("Here are the starting Discamals:")
	add_disc(FREE_ANIMAL_NAMES, USED_ANIMAL_NAMES)
	add_disc(FREE_ANIMAL_NAMES, USED_ANIMAL_NAMES)
	print(USED_ANIMAL_NAMES)
	print ("Lucky Snow would like to offer you these two Discamals free if you agree to participate in our tournament tomorrow!")
	print ("Take today to try them out.")

	test(USED_ANIMAL_NAMES, WINNER)
	while len(FREE_ANIMAL_NAMES) > 0:		
		for _ in range(int((len(USED_ANIMAL_NAMES) - 1)/2)):
			test(USED_ANIMAL_NAMES, WINNER)
		
		tournament(USED_ANIMAL_NAMES, _players, WINNER)
		_new = add_disc(FREE_ANIMAL_NAMES, USED_ANIMAL_NAMES)
		print ("The new discamal is", _new, ". Hope you enjoy it!")

	print ("End of game.")