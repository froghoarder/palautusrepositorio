"""NHL player model."""


class Player:
    """Represent a player's scoring statistics."""

    # This class intentionally models a player with a single display method.
    # pylint: disable=too-few-public-methods
    def __init__(self, player_data):
        self.name = player_data['name']
        self.nationality = player_data['nationality']
        self.assists = player_data['assists']
        self.goals = player_data['goals']
        self.points = self.assists + self.goals

    def __str__(self):
        """Return the player's name and point total."""
        return f"{self.name:21}{self.points:13}"
