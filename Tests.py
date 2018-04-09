import unittest
import DiscamalsGame

class TestDiscamals(unittest.TestCase):
    _usedAnimalNames = []
    _freeAnimalNames = ["testanimal","manytests"]

    def test_AddDisc_AddsDiscToUsedAnimalNames(self):
        length_before = len(self._usedAnimalNames)
        DiscamalsGame.add_disc(self._freeAnimalNames, self._usedAnimalNames)
        unittest.assertEqual(length_before + 1, len(self._usedAnimalNames))

    def test_AddDisc_RemovesDiscFromFreeAnimalNames(self):
        length_before = len(self._freeAnimalNames)
        DiscamalsGame.add_disc(self._freeAnimalNames, self._usedAnimalNames)
        unittest.assertEqual(length_before - 1, len(self._freeAnimalNames))

    def test_GetWinner_WinnerExistsInDict(self):
        pass

if __name__ == '__main__':
    unittest.main()