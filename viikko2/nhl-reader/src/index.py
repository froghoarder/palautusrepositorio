from player import Player, PlayerReader, PlayerStats

def main():
    

    while True:
        season = input("Select season [yyyy-yy]: ")
        print()
        nationality = input("Select nationality [CCC]: ")
        print()
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        for player in players:
            print(player)
            print()

if __name__ == "__main__":
    main()
