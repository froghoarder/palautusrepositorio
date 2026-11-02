import unittest
from statistics_service import SortBy, StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.players = PlayerReaderStub().get_players()
        self.service = StatisticsService(PlayerReaderStub())

    def test_search_returns_players_matching_name(self):
        self.assertEqual(self.service.search("Gretzky").name, "Gretzky")

    def test_search_returns_empty_list_when_no_player_matches(self):
        self.assertIsNone(self.service.search("unknown player"))

    def test_team_returns_players_from_the_requested_team(self):
        self.assertEqual(
            [player.name for player in self.service.team("EDM")],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_team_returns_empty_list_when_team_has_no_players(self):
        self.assertEqual(self.service.team("NYR"), [])

    def test_top_returns_players_in_descending_points_order(self):
        top_players = self.service.top(2)
        self.assertEqual([player.name for player in top_players[:2]], ["Gretzky", "Lemieux"])
        self.assertEqual(
            [player.points for player in top_players],
            sorted((player.points for player in top_players), reverse=True)
        )

    def test_top_returns_the_highest_scoring_player_first(self):
        self.assertEqual(self.service.top(1)[0].name, "Gretzky")

    def test_top_can_sort_by_points(self):
        top_players = self.service.top(3, SortBy.POINTS)
        self.assertEqual(
            [player.name for player in top_players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_can_sort_by_goals(self):
        top_players = self.service.top(3, SortBy.GOALS)
        self.assertEqual(
            [player.name for player in top_players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_can_sort_by_assists(self):
        top_players = self.service.top(3, SortBy.ASSISTS)
        self.assertEqual(
            [player.name for player in top_players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )

    def test_top_returns_requested_number_of_players(self):
        self.assertEqual(len(self.service.top(3)), 3)


if __name__ == "__main__":
    unittest.main()
