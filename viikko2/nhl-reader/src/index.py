"""Run the NHL player statistics reader."""

from rich import print as rich_print
from rich.table import Table
from playerreader import PlayerReader
from playerstats import PlayerStats


def main():
    """Prompt for a season and filter, then display matching scorers."""
    season = input("Season between 2018-2026 in format 2024-25: ")
    if season == "":
        season = "2024-25"

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    filter_type = input("Show players by (1) nationality or (2) team? [1/2]: ")
    if filter_type == "1":
        filter_value = input("Nationality [USA/FIN/CAN/...]: ")
        players = stats.top_scorers_by_nationality(filter_value)
        filter_label = filter_value
    elif filter_type == "2":
        filter_value = input("Team abbreviation [BOS/EDM/...]: ")
        players = stats.top_scorers_by_team(filter_value)
        filter_label = filter_value
    else:
        print("Choose 1 for nationality or 2 for team.")
        return

    table = Table(title=f"Top scorers - {filter_label} ({season})")
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

    rich_print(table)

if __name__ == "__main__":
    main()
