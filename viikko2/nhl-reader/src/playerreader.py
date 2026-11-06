"""Fetch NHL player data from the statistics API."""

import requests
from player import Player


class PlayerReader:
    """Retrieve player records from an NHL statistics URL."""

    # This class intentionally exposes one data-loading operation.
    # pylint: disable=too-few-public-methods
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        """Fetch and convert the players returned by the API."""
        players_json = requests.get(self.url, timeout=10).json()
        players = []
        for p_dict in players_json:
            player = Player(p_dict)
            players.append(player)

        return players
