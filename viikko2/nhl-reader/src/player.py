import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.team = dict["team"]
        self.goals = dict["goals"]
        self.assists = dict["assists"]
        self.points = self.goals + self.assists
    
    def __str__(self):
        return self.name

class PlayerReader:
    def __init__(self, url):
        self.players_dict = requests.get(url).json()
        self.players_all = [Player(p) for p in self.players_dict]

class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        top = []
        for player in self.reader.players_all:
            if player.nationality == nationality:
                top.append(player)

        return sorted(top, key=lambda player: player.points, reverse=True)
