import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_by_name(self):
        result = self.stats.search("Semenko")

        self.assertEqual(str(result), "Semenko EDM 4 + 12 = 16")
    # ...

    def test_false_search_by_name(self):
        result = self.stats.search("Sement")

        self.assertEqual(result, None)

    def test_team_search(self):
        result = self.stats.team("EDM")
        test_output = [str(player) for player in result]

        self.assertEqual(test_output, ["Semenko EDM 4 + 12 = 16", "Kurri EDM 37 + 53 = 90", "Gretzky EDM 35 + 89 = 124"])

    def test_false_team_search(self):
        result = self.stats.team("")

        self.assertEqual(result, [])

    def test_top_valid_input(self):
        result = self.stats.top(3, 1)

        test_output = [str(player) for player in result]

        self.assertEqual(test_output, ["Gretzky EDM 35 + 89 = 124", "Lemieux PIT 45 + 54 = 99", "Yzerman DET 42 + 56 = 98"])


    def test_top_invalid_input_second(self):
        with self.assertRaises(ValueError) as context:
            result = self.stats.top(1, 5)

    def test_sort_by_goals(self):
        result = self.stats.top(3, 2)

        test_output = [str(player) for player in result]

        self.assertEqual(test_output, ["Lemieux PIT 45 + 54 = 99", "Yzerman DET 42 + 56 = 98", "Kurri EDM 37 + 53 = 90"])
    
    def test_sort_by_assists(self):
        result = self.stats.top(3, 3)

        test_output = [str(player) for player in result]

        self.assertEqual(test_output, ["Gretzky EDM 35 + 89 = 124", "Yzerman DET 42 + 56 = 98", "Lemieux PIT 45 + 54 = 99"])
    