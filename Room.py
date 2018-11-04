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

    @staticmethod
    def slow_print(string, sec):
        for i in range(len(string)):
            print(string[i], end="", flush=True)
            time.sleep(sec)

        print("\n")
