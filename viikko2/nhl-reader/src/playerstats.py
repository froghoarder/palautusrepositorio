"""Statistics and filtering for NHL players."""


class PlayerStats:
    """Provide queries over a collection of players."""

    # This class intentionally exposes one query operation.
    # pylint: disable=too-few-public-methods
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        """Return players of the given nationality ordered by points."""
        top_scorers = []
        for pl in self.reader.players:
            if pl.nationality == nat:
                top_scorers.append(pl)

        return sorted(top_scorers, key=lambda x: -x.points)
