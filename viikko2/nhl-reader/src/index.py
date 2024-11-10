from player import Player, PlayerReader, PlayerStats
from rich import print
from rich.console import Console
from rich.table import Table

def create_table(players, nationality, season):
    table = Table(title=f"Top scorers of {nationality} season {season}")
    table.add_column("name", justify="right", style="cyan", no_wrap=True)
    table.add_column("team", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), \
            str(player.assists), str(player.points))
            
    return table

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

        table = create_table(players, nationality, season)
        console = Console()
        console.print(table)

if __name__ == "__main__":
    main()
