# -*- coding: utf-8 -*-
import os.path
import codecs
from Room import Room
from Action import Action

room = Room()
action = []


FILE_NAME = "1.txt"

if os.path.isfile(FILE_NAME):

    with codecs.open(FILE_NAME, "r", "utf-8") as f:
        data = f.readlines()
    f.close()

    if data is not None and len(data) == 324:

        for i in range(len(data)):
            data[i] = data[i].replace("\n", "")
            data[i] = data[i].replace("*a", "ą")
            data[i] = data[i].replace("*A", "Ą")
            data[i] = data[i].replace("*c", "ć")
            data[i] = data[i].replace("*C", "Ć")
            data[i] = data[i].replace("*e", "ę")
            data[i] = data[i].replace("*E", "Ę")
            data[i] = data[i].replace("*l", "ł")
            data[i] = data[i].replace("*L", "Ł")
            data[i] = data[i].replace("*n", "ń")
            data[i] = data[i].replace("*N", "Ń")
            data[i] = data[i].replace("*s", "ś")
            data[i] = data[i].replace("*S", "Ś")
            data[i] = data[i].replace("*o", "ó")
            data[i] = data[i].replace("*O", "Ó")
            data[i] = data[i].replace("*z", "ż")
            data[i] = data[i].replace("*Z", "Ż")
            data[i] = data[i].replace("*x", "ź")
            data[i] = data[i].replace("*X", "Ź")
            data[i] = data[i].replace("\r", "")

        room.add_room(data[0], data[0], data[1].replace("\\n", "\n"))

        for i in range(2, len(data) - 1, 23):
            room.add_room(data[i], data[i + 1], data[i + 2].replace("\\n", "\n"))

            action.append(Action())

            for x in range(3, 23, 5):
                action[len(action)-1].add_action(data[i + x], data[i + x + 1], int(data[i + x + 2]), int(data[i + x + 3]), data[i + x + 4])

            action[len(action)-1].randomize()

    else:
        input("Ktoś majstrowal przy plikach z danymi!")
        exit(0)

else:
    input("Błąd w pliku danych!")
    exit(0)
