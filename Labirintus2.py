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


x = input(szinek['sárga'] + "\nAdd meg a pálya szélességét (a keretet nem bele számítva): ")
while x.isnumeric() == False:
    x = input(szinek['piros'] + "SZÁMOT adjál meg: ")
x = int(x) + 2

y = input(szinek['sárga'] + "Add meg a pálya hosszúságát (a keretet nem bele számítva): ")
while y.isnumeric() == False:
    y = input(szinek['piros'] + "SZÁMOT adjál meg: ")
y = int(y) + 2


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def labirintus_rajz(x, y):

    global labirintus_sor
    global labirintus
    labirintus_sor = []
    labirintus = []
    n = 0

    for oszlop in range(y):
        for sor in range(x):
            if oszlop == 0 or sor == 0:
                labirintus_sor.append(1)
            elif oszlop == y - 1 or sor == x - 1:
                labirintus_sor.append(1)
            else:
                if oszlop == y - 2 and sor == x - 2:
                    labirintus_sor.append("X")
                elif oszlop == 1 and sor == 1:
                    labirintus_sor.append("◯")
                elif random.randint(1, 3) != 1:
                    labirintus_sor.append(0)
                else:
                    labirintus_sor.append(1)

    for index in range(1, (y + 2)):
        labirintus.append(labirintus_sor[n * x:(x * index)])
        n += 1


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#labirintus megrajzolása


    print("Leegyszerűsített labirintus:\n")
    for oszlop in range(y):
        for sor in range(x):
            print(labirintus[oszlop][sor], end="")
        print()


    print("\nLabirintus:\n")

    for oszlop in range(y):
        for sor in range(x):
            if labirintus[oszlop][sor] == 1:
                print(szinek['v_kék'], 1, end="")
            elif labirintus[oszlop][sor] == 0:
                print(szinek['v_kék'], " ", end="")
            elif labirintus[oszlop][sor] == "X":
                print(szinek['v_zöld'], "X", end="")
            elif labirintus[oszlop][sor] == "◯":
                print(szinek['v_piros'], "◯", end="")

        print()


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
    irany = (input(szinek['sárga'] + "\nMerre akarsz mozogni? (fel, le, jobbra, balra): "))
    move(irany)
