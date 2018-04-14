import unittest
import Discamal
import Game

class TestDiscamal(unittest.TestCase):
    def test_NewDicamal_ReturnsNewDiscamal(self):
        factory = Discamal.DiscamalFactory(["test"])
        disc = factory.new_discamal()
        self.assertEqual(disc.name, "test")
        self.assertEqual(disc.tournamentWins, 0)

    def test_NewDiscamalRepeated_ReturnsDifferentDiscs(self):
        factory = Discamal.DiscamalFactory(["test","other"])
        disc = factory.new_discamal()
        other = factory.new_discamal()
        self.assertNotEqual(disc,other)

class TestGame(unittest.TestCase):

    def test_GetWinner_ReturnsOneOfTheInputs(self):
        WinnerList = {}
        team1 = frozenset([Discamal.Discamal("test")])
        team2 = frozenset([Discamal.Discamal("other")])
        result = Game.get_winner(team1, team2, WinnerList)
        self.assertIn(result, [team1,team2])

    def test_GetWinner_IsConsistent(self):
        WinnerList = {}
        team1 = frozenset([Discamal.Discamal("test")])
        team2 = frozenset([Discamal.Discamal("other")])
        first = Game.get_winner(team1, team2, WinnerList)
        second = Game.get_winner(team1, team2, WinnerList)
        self.assertEqual(first, second)

    def test_GetWinner_ChangeOrderIsConsistent(self):
        WinnerList = {}
        team1 = frozenset([Discamal.Discamal("test")])
        team2 = frozenset([Discamal.Discamal("other")])
        first = Game.get_winner(team1, team2, WinnerList)
        second = Game.get_winner(team2, team1, WinnerList)
        self.assertEqual(first, second)

    def test_GetWinner_DominatedTeamLoses(self):
        disc1 = Discamal.Discamal("one")
        disc1t = frozenset([disc1])
        disc2 = Discamal.Discamal("two")
        disc2t = frozenset([disc2])
        disc3 = Discamal.Discamal("three")
        disc3t = frozenset([disc3])
        disc4 = Discamal.Discamal("four")
        disc4t = frozenset([disc4])

        WinnerList = {frozenset([disc1t,disc3t]):disc1t,
                      frozenset([disc1t,disc4t]):disc1t,
                      frozenset([disc2t,disc3t]):disc2t,
                      frozenset([disc2t,disc4t]):disc2t}
        team1 = frozenset([disc1,disc2])
        team2 = frozenset([disc3,disc4])
        self.assertEqual(Game.get_winner(team1, team2, WinnerList), team1)

    def test_FormatTeam_ReturnsNameList(self):
        team = frozenset( [Discamal.Discamal("one"),  Discamal.Discamal("two")] )
        self.assertIn(Game.format_team(team), ["one two", "two one"])

if __name__ == '__main__':
    unittest.main()
