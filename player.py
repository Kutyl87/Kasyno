from random import choices


class Player:
    def __init__(self, player_name):
        self._player_name = player_name
        self._player_points = 0
        self._player_pointslist = []
        self._player_id = None

    @property
    def player_name(self):
        return self._player_name

    @property
    def player_points(self):
        return self._player_points

    @property
    def player_pointslist(self):
        return self._player_pointslist

    @property
    def id(self):
        return self._player_id

    def __lt__(self, other: "Player"):
        return self.player_points < other.player_points

    def __eq__(self, other: "Player"):
        return self.player_points == other.player_points

    def _count_points(self, points_list):
        criteria_dictionary = {
            "pair_criteria": sum(elem*2 if points_list.count(elem) == 2 else 0 for elem in set(points_list)),
            "three_criteria": max(points_list, key=points_list.count) * 4 if points_list.count(max(points_list, key=points_list.count)) == 3 else 0,
            "four_criteria": max(points_list, key=points_list.count)*6 if len(set(points_list)) == 1 else 0,
            "even_criteria": sum(points_list)+2 if sum(elem % 2 for elem in points_list) == 0 else 0,
            "odd_criteria": sum(points_list)+3 if sum(elem % 2 for elem in points_list) == 4 else 0,
        }
        return max(criteria_dictionary.values())

    def player_set_id(self, id):
        self._player_id = id

    def throw_a_cube(self):
        current_throw = choices([*range(1, 7)], k=4)
        self._player_points += self._count_points(current_throw)
        self._player_pointslist += current_throw


def main():
    player = Player("Ania")
    print(player.throw_a_cube())
    print()


if __name__ == "__main__":
    main()
