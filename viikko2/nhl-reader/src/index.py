from rich import print
from rich.table import Table
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    season = input("Season between 2018-2026 in format 2024-25: ")
    if season == "":
        season = "2024-25"

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = input("Nationality [USA/FIN/CAN/...]: ")

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Top scorers - {nationality} ({season})")
    table.add_column("#", justify="right", style="dim")
    table.add_column("Player", style="bold")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right", style="bold green")

    for rank, player in enumerate(players, start=1):
        table.add_row(
            str(rank),
            player.name,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    print(table)

if __name__ == "__main__":
    main()
