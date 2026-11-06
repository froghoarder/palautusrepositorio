import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = self.get_players()

    def get_players(self):
        players_json = requests.get(self.url).json()
        players = []
        for p_dict in players_json:
            player = Player(p_dict)
            players.append(player)

        return players

