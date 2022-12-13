from player import Player
from errors import WrongPlayersNumber, PlayerNotFound


class Casino:
    def __init__(self, player_list, number_of_rounds=1):
        self._player_list = player_list
        self._number_of_rounds = number_of_rounds
        for id, player in enumerate(self._player_list):
            player.player_set_id(id+1)

    def find_cur_winner(self):
        curr_points = [person.player_points for person in self._player_list]
        if curr_points.count(max(self._player_list).player_points) > 1:
            return None
        else:
            return max(self._player_list).player_name

    def formate_winniners(self, winner, i):
        if winner:
            return f"Po {i} roundzie wygrywa {winner}"
        else:
            return f"Po {i} rundzie mamy remis"

    def find_max_id(self):
        return max(player.id for player in self._player_list)

    def add_player(self, player):
        player.player_set_id(self.find_max_id()+1)
        self._player_list.append(player)

    def remove_player(self, id):
        tempororary_list = self._player_list
        self._player_list = [
            player for player in self._player_list if player.id != id]
        if len(tempororary_list) == len(self._player_list):
            raise PlayerNotFound(id)

    def show_info_about_throws(self, person):
        return f'{person.player_name} wyrzucił/a {" ".join(str(elem) for elem in (person.player_pointslist)[-4:])} co daje {person._count_points((person.player_pointslist)[-4:])} punktów.'

    def show_current_points(self):
        return "\n".join([(person.player_name+" : "+str(person.player_points)) for person in self._player_list])

    def show_players_id(self):
        return " ".join(f"{player.player_name} : {player.id}" for player in self._player_list)

    def run_game(self):
        if len(self._player_list) < 2:
            raise WrongPlayersNumber(self._player_list)
        for i in range(1, self._number_of_rounds+1):
            for person in self._player_list:
                person.throw_a_cube()
                print(self.show_info_about_throws(person))
            print(self.show_current_points())
            print(self.formate_winniners(self.find_cur_winner(), i))
            print("------------------------------------------------")
        if self._player_list.count(max(self._player_list)) == 1:
            print(f"Zwycięzył {max(self._player_list).player_name}")
        else:
            print("Gra nieroztrzygnięta")


def main():
    player1 = Player("Monika")
    player2 = Player("Ania")
    casino = Casino([player1, player2], 8)
    casino.run_game()


if __name__ == "__main__":
    main()
