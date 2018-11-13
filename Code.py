# -*- coding: utf-8 -*-
import random as r
import os
import Addons

code = ""
unknown = []
boss_name = ""
boss_pict = ""


def generate(amount):
    global code
    global unknown
    code = ""
    unknown = []
    for i in range(amount):
        code += str(r.randint(1, 9))

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


def return_known_code():
    know = list(code)

    for i in unknown:
        for x in range(len(i)):
            if i[x] != "*":
                know[x] = "*"
                break
    know = "".join(know)
    return know


def ending(player):
    sec = 0.005
    while True:
        os.system('cls')
        print("-" * 20)
        Addons.slow_print("""Jesteś w pokoju przeznaczenia\n
Twoje serce zaczyna bić szybciej. Przed Tobą znajdują się duże straszliwe wrota.
Wygląda na to że, aby je otworzyć należy podać odpowiedni kod.""", sec, newline=False)
        if return_known_code() == code:
            print("\nZnasz już cały kod: " + code)
        else:
            print("\nZnasz część cyfr kodu: " + return_known_code())

        Addons.slow_print("""Jednak czy jesteś na tyle odważny aby przekonać się co kryje się za tymi drzwiami?
Widzisz, że masz też prawdopodobną możliwość powrotu przez ten sam portal,
z którego tu przyszedłeś.""", sec)
        sec = 0
        print("Co robisz? (1/2)\n")
        print("1. Próbujesz wpisać kod")
        print("2. Wchodzisz do portalu")
        p = input(">>>")

        if p == "1":
            if guess(player) == 1:
                return 1

        elif p == "2":
            Addons.slow_print("Portal przenosi Cię do pokoju startowego.\n", 0.05)
            input("\nWciśnij ENTER, aby kontunuować...")
            return 0


def guess(player):
    print("\nPodaj kod")
    code1 = input(">>>")

    if code == code1:
        print("Podałeś właściwy Kod.")
        Addons.slow_print("Wrota otwierają się z wielkim piskiem...\n" + boss_name + " chce pożreć Twoją duszę!", 0.1)
        Addons.slow_print(boss_pict, 0.0001)
        input("\nWciśnij ENTER, aby kontunuować...")

        player.attack(boss_name, r.randint(8 + player.lvl, 13 + player.lvl) * 10)
        if not player.dead:
            Addons.print_congrats()
            print("\nKONIEC GRY")
            player.save_score()
            input("\nWciśnij ENTER, aby kontunuować...")
        os.system('cls')
        return 1

    else:
        print("\nZły kod.\nZ podłogi wysuwają się kłujące kolce.\n")
        player.update_hp(10)
        input("\nWciśnij ENTER, aby kontunuować...")
        return 0
