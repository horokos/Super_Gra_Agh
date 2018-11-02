# -*- coding: utf-8 -*-


class Struktura:
    def __init__(self):
        self.id_room = 1

    def p_move(self, room):
        while True:
            print("-"*20 + "\nGdzie się ruszasz? (1/2/3)\n")
            print("1. " + room.rooms_names[self.id_room * 2 + - 1])
            print("2. " + room.rooms_names[self.id_room * 2])
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

            if move == "4":
                break
