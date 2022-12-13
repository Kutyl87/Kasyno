from player import Player


def test_constructor():
    player = Player("Mirek")
    assert player.player_name == "Mirek"
    assert player.player_points == 0
    assert player.player_pointslist == []


def test_coutning_points():
    player = Player("Mirek")
    assert player._count_points([6, 6, 6, 2]) == 24
    assert player._count_points([1, 1, 1, 1]) == 7
    assert player._count_points([6, 6, 6, 6]) == 36
    assert player._count_points([2, 2, 2, 2]) == 12
    assert player._count_points([2, 4, 2, 4]) == 14
    assert player._count_points([6, 1, 3, 5]) == 0
    assert player._count_points([4, 2, 2, 6]) == 16
    assert player._count_points([5, 5, 5, 5]) == 30
    assert player._count_points([5, 5, 1, 3]) == 17
    assert player._count_points([6, 6, 3, 3]) == 18


def test_throw_a_cube_ones(monkeypatch):
    player = Player("Jurij")

    def returnones(f, k):
        return [1, 1, 1, 1]
    monkeypatch.setattr("player.choices", returnones)
    player.throw_a_cube()
    assert player._player_pointslist == [1, 1, 1, 1]


def test_throw_a_cube_diff(monkeypatch):
    player = Player("Jurij")

    def returndiff(f, k):
        return [3, 5, 1, 5]
    monkeypatch.setattr("player.choices", returndiff)
    player.throw_a_cube()
    assert player._player_pointslist == [3, 5, 1, 5]


def test_throw_a_cube_sixs(monkeypatch):
    player = Player("Jurij")

    def returnsixs(f, k):
        return [6, 6, 6, 6]
    monkeypatch.setattr("player.choices", returnsixs)
    player.throw_a_cube()
    assert player._player_pointslist == [6, 6, 6, 6]


def test_compare(monkeypatch):
    player1 = Player("Ania")
    player2 = Player("Monika")

    def returnsixs(f, k):
        return [6, 6, 6, 6]
    monkeypatch.setattr("player.choices", returnsixs)
    player1.throw_a_cube()
    player1.throw_a_cube()
    player2.throw_a_cube()
    assert player2 < player1
    assert player1 > player2
    player2.throw_a_cube()
    assert player1 == player2


def test_monkey(monkeypatch):
    player1 = Player("Ania")
    player2 = Player("Monika")

    def returnsixs(f, k):
        return [6, 6, 6, 6]
    monkeypatch.setattr("player.choices", returnsixs)
    player1.throw_a_cube()
    assert player1.player_points == 36

    def returnodds(f, k):
        return [1, 3, 5, 5]
    monkeypatch.setattr("player.choices", returnodds)
    player2.throw_a_cube()
    assert player2.player_points == 17
    assert player1 > player2
