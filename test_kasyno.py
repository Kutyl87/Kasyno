from kasyno import Casino
import pytest
from errors import WrongPlayersNumber
from player import Player


def test_not_enough_players():
    casino = Casino([Player("Ania")])
    with pytest.raises(WrongPlayersNumber) as e:
        casino.run_game()
        assert str(e.value) == "Do gry potrzeba min. 2 graczy"


def test_not_enough_players_2ndvers():
    casino = Casino([Player("Ania")])
    casino.add_player(Player("Mirek"))
    casino.run_game()
    with pytest.raises(WrongPlayersNumber) as e:
        casino.remove_player(1)
        casino.run_game()
        assert str(e.value) == "Do gry potrzeba min. 2 graczy"


def test_showing_ids():
    casino = Casino([Player("Ania")])
    casino.add_player(Player("Mirek"))
    assert casino.show_players_id() == "Ania : 1 Mirek : 2"
