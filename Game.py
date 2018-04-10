from random import choice
from random import choices
from Player import *
from Discamal import *

#TODO do these need to be globals, or can they be shoved into the __main__ method?
ANIMAL_NAMES = ["bear", "chickadee", "cougar", "coyote", "crow", "duck", "goose", "lynx", "orca", "raccoon", "raven", "seagull", "squirrel" ]
DISC_LIST = []
WINNER = {}

def add_disc(DiscFactory):
	_new_disc = DiscFactory.new_discamal()
	print("New disc is %s" % _new_disc.name)
	DISC_LIST.append(_new_disc)
	return _new_disc

#Teams are frozensets.
def get_winner(Team1, Team2, WinnerList):
	#TODO is a case for a "bye" needed here?
	if len(Team1) != len(Team2) or Team1 == Team2:
		raise Exception()

	if  ( not (frozenset([Team1,Team2]) in WinnerList) ):
		if (len(Team1) == 1):
			WinnerList[frozenset([Team1,Team2])] = choice([Team1,Team2])

		else:
			_score1 = 0
			_score2 = 0
			for (_disc1, _disc2) in [(x,y) for x in Team1 for y in Team2]:
				if ( _disc1 == _disc2 ):
					continue
				elif ( get_winner( frozenset([_disc1]), frozenset([_disc2]), WinnerList ) == frozenset([_disc1]) ):
					_score1 += 1
				else:
					_score2 += 1

			WinnerList[frozenset([Team1,Team2])] = choices([Team1,Team2], [_score1, _score2])[0]

	return WinnerList[frozenset([Team1,Team2])]

#TODO parse input in a better way
#TODO print messages out in a way that's easier to read
def test(PlayersDiscamals, WinnerList):
	print ("Choose two teams to discover the winner.")

	_team_size = None
	while not (type(_team_size) == int):
		_team_size = input("Enter the size of team do you want to test: ")
		try:
			_team_size = int(_team_size)
		except (Exception):
			print ("Please enter a valid integer.")

	print ("First Team")
	_d1 = select_team_manually(PlayersDiscamals, _team_size)
	print ("Second Team")
	_d2 = select_team_manually(PlayersDiscamals, _team_size)

	print("%s wins the test." % format_team(get_winner(_d1, _d2, WinnerList)))

	print("")

#TODO add ai that choose teams smarter (right now just random)
def tournament(AvailableDiscamals, Players, WinnerList, TeamSize):
	print("Choose a team of %s Discamals to take to the tournament." % TeamSize)
	for player in Players:
		player.select_team(AvailableDiscamals, TeamSize)

	#this is just a work around until tounament code is improved.
	#for now single elim. plan is swiss to top x (8?)
	_winner = single_elim(Players, WinnerList)
	for _disc in _winner.currentTeam:
		_disc.tournamentWins += 1
	print ("%s won the tournament with %s." % (_winner.name, format_team(_winner.currentTeam)))

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

	return _cur_round[0]

def format_team(Team):
	return ' '.join(map(str,Team))

#TODO Some sort of economy
#TODO Different number of tests/tournaments as the number of discamals goes up.
if __name__ == '__main__':
	_players = [Player(input("Please enter your name:"), select_team_manually),
			    Player("Randy", select_team_randomly),
			    Player("Andy", select_team_randomly),
			    Player("Mandy", select_team_most_wins)]
	_disc_factory = DiscamalFactory(ANIMAL_NAMES)

	print ("Here are the starting Discamals:")
	add_disc(_disc_factory)
	add_disc(_disc_factory)
	print ("Lucky Snow would like to offer you these two Discamals free if you agree to participate in our tournament tomorrow!")
	print ("Take today to try them out.")

	test(DISC_LIST, WINNER)
	while True:
		for _ in range(int((len(DISC_LIST) - 1)/2)):
			test(DISC_LIST, WINNER)

		#TODO better team size selection.
		#	  want there to still be some 1's, but later should be more 2's or even 3's
		_team_size  = choice([1,2])
		tournament(DISC_LIST, _players, WINNER, _team_size)
		_new = add_disc(_disc_factory)
		print ("The new discamal is %s. Hope you enjoy it!" % _new)

	print ("End of game.")
