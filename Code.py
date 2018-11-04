# -*- coding: utf-8 -*-
import random as r

code = str()
unknown = list()


def generate():
    code = "%s%s%s%s%s" % (r.randint(1, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9))

    for i in range(len(code)):
        unknown.append("*" * i + code[i] + "*" * (len(code) - i - 1))


def get_rand_num():
    if len(unknown) > 0:
        num = r.choice(unknown)
        unknown.remove(num)
        return "\"Kod: " + num + "\"\n"
    else:
        return "Kod: " + code


def guess(player):
    while True:
        print("Podaj kod")
        code1 = input(">>>")

        if code == code1:
            print("Podałeś właściwy szyfr.")
            break
        else:
            print("Zły kod.\nZ podłogi wysuwają się kłujące kolce.")
            player.update_hp(10)
