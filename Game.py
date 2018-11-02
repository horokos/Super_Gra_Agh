import os
from Struktura import Struktura
from Player import Player
from Load import room
from Load import action


player = Player()
a = Struktura()


while True:
    a.p_move(room)
    os.system('cls')
    room.introduce(a.id_room - 1)

    if a.id_room > 1:
        action[a.id_room - 2].do_action(player)
