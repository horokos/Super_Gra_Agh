from Struktura import Struktura
from Player import Player
from Load import room
from Load import action


player = Player()
a = Struktura()


while True:
    a.p_move()
    room.introduce(a.id_room - 1)

    if a.id_room > 1:
        action[a.id_room - 2].print_actions()
        action[a.id_room - 2].do_action(player)
