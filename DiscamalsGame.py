from random import choice

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

#TODO Implement the way to determine winners from teams
def get_winner(Team1, Team2, WinnerList):
	Team1 = frozenset([Team1])
	Team2 = frozenset([Team2])

	if len(Team1) != len(Team2) or Team1 == Team2:
		return None

	if  ( not (frozenset([Team1,Team2]) in WinnerList) ):
		#TODO right now this will always be true, because we take frozenset([team]). Need some sort of check if it's just a string before frozensetting.
		if (len(Team1) == 1):
			WinnerList[frozenset([Team1,Team2])] = choice([Team1,Team2])

		#TODO implement this
		else:
			pass

	return WinnerList[frozenset([Team1,Team2])]

#TODO parse input in a better way
#TODO print messages out in a way that's easier to read
def test(PlayersDiscamals, WinnerList):
	print ("Choose two Discamals to discover the winner.")
	
	#shouldn't let player choose same disc twice
	#TODO check that the input is valid before moving on
	_d1 = choose_disc(PlayersDiscamals, "First  Discamal:")
	_d2 = choose_disc([d for d in PlayersDiscamals if d!=_d1], "Second Discamal:")

	for _disc in get_winner(_d1, _d2, WinnerList):
		print(_disc)

	print("")

#TODO make tournaments team rather than just 1v1s
#TODO add ai that choose teams smarter (right now just random)
#TODO make tournaments more than just a single match
def tournament(PlayersDiscamals, UsedAnimalNames, WinnerList):
	_dplayer = choose_disc(PlayersDiscamals, "Choose a Discamal to take to the tournament:")
	_dcomp = choice(UsedAnimalNames)

	print ("Your opponent chose", _dcomp)
	if (_dplayer == _dcomp):
		_player_wins = choice([True, False])
		if (_player_wins):
			print("Lucky you won the mirror match!")
		else:
			print("Unfortunately you lost the mirror match.")

	elif (get_winner(_dplayer, _dcomp, WinnerList) == frozenset([_dplayer])):
		print("And you win!")
	else:
		print ("You lose.")

	print("")

#TODO implement a trie based name-checker, to make inputs easier (don't have to type whole thing)
def choose_disc(PlayersDiscamals, msg):
	_dplayer = ""
	while (not _dplayer in PlayersDiscamals):
		_dplayer = input(msg).lower()

	return _dplayer

#TODO Some sort of economy
#TODO Different number of tests/tournaments as the number of discamals goes up.
if __name__ == '__main__':
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
		
		tournament(USED_ANIMAL_NAMES, USED_ANIMAL_NAMES, WINNER)
		_new = add_disc(FREE_ANIMAL_NAMES, USED_ANIMAL_NAMES)
		print ("The new discamal is", _new, ". Hope you enjoy it!")

	print ("End of game.")