class WrongPlayersNumber(Exception):
    def __init__(self, players_number):
        super().__init__("Do gry potrzeba min. 2 graczy")
        self._players_number = players_number


class PlayerNotFound(Exception):
    def __init__(self, id):
        super().__init__("Nie znaleziono gracza z tym id")
        self._id = id
