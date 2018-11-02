# -*- coding: utf-8 -*-


class Room:
    def __init__(self):
        self.rooms_names = []
        self.rooms_doors = []
        self.rooms_description = []

    def add_room(self, name, doors, description):
        self.rooms_names.append(name)
        self.rooms_doors.append(doors)
        self.rooms_description.append(description)

    def introduce(self, num):
        print("-"*20)
        print("Jesteś w " + self.rooms_names[num])
        print(self.rooms_description[num] + "\n")

