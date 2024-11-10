import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        if player_dict["nationality"] == "FIN":
            player = Player(player_dict)
            players.append(player)

    print("""Players from FIN\n""")
    
    for player in sorted(players, key=lambda player: player.points, reverse=True):
        print(f"{player.name:20}{player.team:6}{player.points}")

if __name__ == "__main__":
    main()
