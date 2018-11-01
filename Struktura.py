# -*- coding: utf-8 -*-


class Struktura:
    def __init__(self):
        self.id_room = 1

    def p_move(self):
        while True:
            move = input("Gdzie się ruszasz? (p/l/t)\n")

            if move.upper() == "P":
                self.id_room = self.id_room * 2 + 1
                break

            if move.upper() == "L":
                self.id_room *= 2
                break

            if move.upper() == "T":
                if self.id_room != 1:
                    self.id_room = int(self.id_room / 2)
                    break
                else:
                    print("Nie możesz zawrócić!")
