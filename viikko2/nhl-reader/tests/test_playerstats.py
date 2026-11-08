"""Unit tests for PlayerStats."""

import unittest

from src.player import Player
from src.playerstats import PlayerStats


class PlayerReaderStub:
    """Provide player data without making an API request."""

    def __init__(self, players):
        self.players = players


class PlayerStatsTest(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Alex",
                "team": "AAA",
                "nationality": "FIN",
                "assists": 8,
                "goals": 5,
            }),
            Player({
                "name": "Blake",
                "team": "BBB",
                "nationality": "FIN",
                "assists": 4,
                "goals": 10,
            }),
            Player({
                "name": "Casey",
                "team": "AAA",
                "nationality": "USA",
                "assists": 12,
                "goals": 3,
            }),
            Player({
                "name": "Drew",
                "team": "AAA",
                "nationality": "FIN",
                "assists": 2,
                "goals": 7,
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_top_scorers_by_nationality_filters_and_orders_by_points(self):
        scorers = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(["Blake", "Alex", "Drew"], [player.name for player in scorers])
        self.assertEqual([14, 13, 9], [player.points for player in scorers])

    def test_top_scorers_by_team_filters_and_orders_by_points(self):
        scorers = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(["Casey", "Alex", "Drew"], [player.name for player in scorers])
        self.assertEqual([15, 13, 9], [player.points for player in scorers])

    def test_top_goal_scorers_orders_by_goals_and_limits_results(self):
        scorers = self.stats.top_goal_scorers(2)

        self.assertEqual(["Blake", "Drew"], [player.name for player in scorers])
        self.assertEqual([10, 7], [player.goals for player in scorers])


if __name__ == "__main__":
    unittest.main()
