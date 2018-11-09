# -*- coding: utf-8 -*-
import random as r

code = str()
unknown = list()


def generate():
    global code
    global unknown
    code = "%s%s%s%s%s" % (r.randint(1, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9), r.randint(1, 9))

    for i in range(len(code)):
        unknown.append("*" * i + code[i] + "*" * (len(code) - i - 1))


def get_rand_num():
    global unknown
    if len(unknown) > 0:
        num = r.choice(unknown)
        unknown.remove(num)
        return "\"Kod: " + num + "\"\n"
    else:
        return "Kod: " + code


def ending(player):
    print("-"*20)
    print("Przed Tobą znajdują się duże wrota otwirane kodem, a za Tobą portal.\n")
    while True:
        print("\n\nCo robisz? (1/2)\n")
        print("1. Próbujesz wpisać kod")
        print("2. Wchodzisz to portalu")
        p = input(">>>")

        if p == "1":
            if guess(player) == 1:
                return 1

        elif p == "2":
            print("Portal przenosi Cię do pokoju startowego.\n\n")
            input("\nWciśnij ENTER, aby kontunuować...")
            return 0

        else:
            print("Zła wartość!\n")


def guess(player):
    print("\nPodaj kod")
    code1 = input(">>>")

    if code == code1:
        boss_name = r.choice(["Wilkorz"])
        print("Podałeś właściwy szyfr.")
        print("Wrota otwierają się\n" + boss_name + " chce pożreć Twoją duszę!")
        player.attack(boss_name, r.randint(8 + player.lvl, 13 + player.lvl) * 10)
        return 1

    else:
        print("Zły kod.\nZ podłogi wysuwają się kłujące kolce.")
        player.update_hp(10)
        return 0
