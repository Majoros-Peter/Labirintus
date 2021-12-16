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


print(szinek['sárga'] + "\nÜDV A LABIRINTUS NEVŰ JÁTÉKBAN!\n")
print("Ahoz, hogy nyerj, el kell juttatnod a "+ szinek['v_zöld'] + "X" + szinek['sárga'] + "-et a " + szinek['v_piros'] + "◯" + szinek['sárga'] + "-höz.")
print("Az mozgás a " + szinek['v_kék'] + "'fel'" + szinek['sárga'] + ", " + szinek['v_kék'] + "'le'" + szinek['sárga'] + ", " + szinek['v_kék'] + "'jobb'" + szinek['sárga'] + ", " + szinek['v_kék'] + "'bal'" + szinek['sárga'] + " szavak beírásával működik.")
print("Sok sikert!\n")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

x = input(szinek['sárga'] + "\nAdd meg a pálya szélességét (a keretet nem bele számítva): ")
while x.isnumeric() == False:
    x = input(szinek['piros'] + "SZÁMOT adjál meg: ")
x = int(x) + 2

y = input(szinek['sárga'] + "Add meg a pálya magasságát (a keretet nem bele számítva): ")
while y.isnumeric() == False:
    y = input(szinek['piros'] + "SZÁMOT adjál meg: ")
y = int(y) + 2

x_sor = 0
x_oszlop = 0


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def main(x, y):

    global labirintus_sor
    global labirintus
    global x_sor
    global x_oszlop
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

def rajz():
    global x_oszlop
    global x_sor
    '''print("Leegyszerűsített labirintus:\n")
    for oszlop in range(y):
        for sor in range(x):
            print(labirintus[oszlop][sor], end="")
        print()'''


    print("\nLabirintus:\n")

    for oszlop in range(y):
        for sor in range(x):
            if labirintus[oszlop][sor] == 1:
                print(szinek['v_kék'] + "1", end="")
            elif labirintus[oszlop][sor] == 0:
                print(szinek['v_kék'] + " ", end="")
            elif labirintus[oszlop][sor] == "X":
                print(szinek['v_zöld'] + "X", end="")
                x_oszlop = oszlop
                x_sor = sor
            elif labirintus[oszlop][sor] == "◯":
                print(szinek['v_piros'] + "◯", end="")

        print()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def move(mozgas):

    global run
    run = True

    if mozgas == "fel":
        if labirintus[x_oszlop - 1][x_sor] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop - 1][x_sor] == "◯":
            print(szinek['v_zöld'] + "NYERTÉL!")
            run = False
        else:
            print("fel")
            labirintus[(x_oszlop - 1)].pop(x_sor)
            labirintus[(x_oszlop - 1)].insert(x_sor, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "le":
        if labirintus[x_oszlop + 1][x_sor] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop + 1][x_sor] == "◯":
            print(szinek['v_zöld'] + "NYERTÉL!")
            run = False
        else:
            print("le")
            labirintus[x_oszlop + 1].pop(x_sor)
            labirintus[x_oszlop + 1].insert(x_sor, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "jobb":
        if labirintus[x_oszlop][x_sor + 1] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop][x_sor + 1] == "◯":
            print(szinek['v_zöld'] + "NYERTÉL!")
            run = False
        else:
            print("jobb")
            labirintus[x_oszlop].pop(x_sor + 1)
            labirintus[x_oszlop].insert(x_sor + 1, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "bal":
        if labirintus[x_oszlop][x_sor - 1] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop][x_sor - 1] == "◯":
            print(szinek['v_zöld'] + "NYERTÉL!")
            run = False
        else:
            print("bal")
            labirintus[x_oszlop].pop(x_sor - 1)
            labirintus[x_oszlop].insert(x_sor - 1, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "exit":
        run = False
    else:
        print(szinek['piros'] + "Ez nem egy opció!\n")


print()

main(x, y)

run = True
while run:
    rajz()
    irany = (input(szinek['sárga'] + "\nMerre akarsz mozogni? (fel, le, jobb, bal): "))
    move(irany)
