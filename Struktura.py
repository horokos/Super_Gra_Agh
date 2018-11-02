# -*- coding: utf-8 -*-
import os
from Load import room
from Load import action


class Struktura:
    def __init__(self):
        self.id_room = 1

    def p_move(self, player):
        while True:
            os.system('cls')
            room.introduce(self.id_room - 1)

            if self.id_room < 8:
                print("-"*20 + "\nGdzie się ruszasz? (1/2/3)\n")
                print("1. " + room.rooms_doors[self.id_room * 2 + - 1])
                print("2. " + room.rooms_doors[self.id_room * 2])
                print("3. Zawróć")

                if self.id_room > 1:
                    print("\nLub...\n4. Wykonaj akcje\n")

                move = input(">>>")

                if move == "1":
                    self.id_room *= 2
                    break

                if move == "2":
                    self.id_room = self.id_room * 2 + 1
                    break

                if move == "3":
                    if self.id_room != 1:
                        self.id_room = int(self.id_room / 2)
                        break
                    else:
                        print("Nie możesz zawrócić!")

                if move == "4" and self.id_room > 1:
                    action[self.id_room - 2].do_action(player, room, self.id_room - 1)
                    break

            else:
                print("-" * 20 + "\nGdzie się ruszasz? (1/2)\n")
                print("1. Wejdź do portalu")
                print("2. Zawróć")
                print("\nLub...\n3. Wykonaj akcje\n")

                move = input(">>>")

                if move == "1":
                    input("Podaj kod")
                    exit(0)
                    break

                if move == "2":
                    self.id_room = int(self.id_room / 2)
                    break

                if move == "3":
                    action[self.id_room - 2].do_action(player, room, self.id_room - 1)
                    break

    os.system('cls')
