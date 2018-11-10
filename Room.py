# -*- coding: utf-8 -*-
import time


class Room:
    def __init__(self):
        self.rooms_names = []
        self.rooms_doors = []
        self.rooms_description = []

    def add_room(self, name, doors, description):
        self.rooms_names.append(name)
        self.rooms_doors.append(doors)
        self.rooms_description.append(description)

    def introduce(self, num, sec):
        print("-"*20)
        self.slow_print("Jesteś w " + self.rooms_names[num], sec)
        self.slow_print(self.rooms_description[num], sec)

    def start(self):
        print("-" * 20)
        self.slow_print(self.rooms_doors[0], 0.001)
        input("\n\nWciśnij ENTER, aby kontynuować...")

    @staticmethod
    def slow_print(string, sec):
        for i in range(0, len(string) - 2, 3):
            print(string[i], end="", flush=True)
            print(string[i + 1], end="", flush=True)
            print(string[i + 2], end="", flush=True)
            time.sleep(sec)

        if len(string) % 3 == 1:
            print(string[len(string) - 1], end="", flush=True)
        elif len(string) % 3 == 2:
            print(string[len(string) - 2], end="", flush=True)
            print(string[len(string) - 1], end="", flush=True)

        print("\n")
