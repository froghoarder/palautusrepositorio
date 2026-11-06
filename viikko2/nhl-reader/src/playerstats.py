class PlayerStats:
    
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        top_scorers = []
        for pl in self.reader.players:
            if pl.nationality == nat:
                top_scorers.append(pl)

        return sorted(top_scorers, key=lambda x: -x.points)

