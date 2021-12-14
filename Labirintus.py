import random

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Sakk.py-ból :)

szinek = {
    'fekete': '\033[30m',
    'piros': '\033[31m',
    'zöld': '\033[32m',
    'narancs': '\033[33m',
    'kék': '\033[34m',
    'lila': '\033[35m',
    'ciánkék': '\033[36m',
    'v_szürke': '\033[37m',
    's_szürke': '\033[90m',
    'v_piros': '\033[91m',
    'v_zöld': '\033[92m',
    'sárga': '\033[93m',
    'v_kék': '\033[94m',
    'rózsaszin': '\033[95m',
    'v_ciánkék': '\033[96m',
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


x = input(szinek['sárga'] + "Add meg a pálya szélességét (pl. 5 -> egy 5x? nagyságú labirintust fog felrajzolni): ")
while x.isnumeric() == False:
    x = input(szinek['piros'] + "SZÁMOT adjál meg: ")
x = int(x)

y = input(szinek['sárga'] + "Add meg a pálya hosszúságát (pl. 6 -> egy ?x6 nagyságú labirintust fog rajzolni): ")
while y.isnumeric() == False:
    y = input(szinek['piros'] + "SZÁMOT adjál meg: ")
y = int(y)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def labirintus_rajz(x, y):

    global labirintus
    global reszekre_bontott_lab
    labirintus = []
    reszekre_bontott_lab = []
    n = 0

    for oszlop in range(y):
        for sor in range(x):
            if random.randint(1, 3) != 1:
                labirintus.append(0)
            else:
                labirintus.append(1)

    for index in range(1, (y + 1)):
        reszekre_bontott_lab.append(labirintus[n * x:(x * index)])
        n += 1


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#labirintus megrajzolása

    reszekre_bontott_lab[-1].pop(-1)
    reszekre_bontott_lab[-1].append("X")

    print(szinek['sárga'] + "┌", end="")
    for index in range(x):
        if reszekre_bontott_lab[0][index] == 1:
            print("─┬", end="")
        else:
            print("──", end="")
    print("┐")

    for oszlop_index in range(y):
        if reszekre_bontott_lab[oszlop_index][0] == 1:
            print(szinek['sárga'] + "├", end="")
        else:
            print(szinek['sárga'] + "│", end="")

        for sor_index in range(x):
            if reszekre_bontott_lab[oszlop_index][sor_index] == 1:
                if sor_index == 0:
                    if oszlop_index == 0:
                        print(szinek['sárga'], "┘", end="")
                    else:
                        print(szinek['sárga'], "─", end="")
                else:
                    print(szinek['sárga'], "│", end="")
                if sor_index == -1:
                    if oszlop_index == 0:
                        print(szinek['sárga'], "└", end="")
                    else:
                        print(szinek['sárga'], "─", end="")
            if reszekre_bontott_lab[oszlop_index][sor_index] == "X":
                print(szinek['v_zöld'], "X", end="")
            if reszekre_bontott_lab[oszlop_index][sor_index] == 0:
                print("  ", end="")

        if reszekre_bontott_lab[oszlop_index][-1] == 1:
            print(szinek['sárga'] + "┤")
        else:
            print(szinek['sárga'] + "│")

    print(szinek['sárga'] + "└", end="")
    for index in range(x):
        if reszekre_bontott_lab[-1][index] == 1:
            print("─┴", end="")
        else:
            print("──", end="")
    print("┘")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#def jatekos_helye():



def move(mozgas):
    if mozgas == "fel":
        print("fel\n")
    elif mozgas == "le":
        print("le\n")
    elif mozgas == "jobbra":
        print("jobbra\n")
    elif mozgas == "balra":
        print("balra\n")
    elif mozgas == "exit":
        run = False
    else:
        print(szinek['piros'] + "Ez nem egy opció!\n")


print()

labirintus_rajz(x, y)

run = True
while run:
    irany = (input(szinek['sárga'] + "Merre akarsz mozogni? (fel, le, jobbra, balra): "))
    move(irany)
