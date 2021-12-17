import random

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Sakk.py-ból (karakterek színezése)

szinek = {
    'piros': '\033[31m',
    'v_piros': '\033[91m',
    'v_zöld': '\033[92m',
    'sárga': '\033[93m',
    'v_kék': '\033[94m',
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Instrukciók:

print(szinek['sárga'] + "\nÜDV A LABIRINTUS NEVŰ JÁTÉKBAN!\n")
print("Ahoz, hogy nyerj, el kell juttatnod a "+ szinek['v_zöld'] + "X" + szinek['sárga'] + "-et a " + szinek['v_piros'] + "◯" + szinek['sárga'] + "-höz.")
print("Az mozgás a " + szinek['v_kék'] + "fel" + szinek['sárga'] + ", " + szinek['v_kék'] + "le" + szinek['sárga'] + ", " + szinek['v_kék'] + "jobb" + szinek['sárga'] + " és " + szinek['v_kék'] + "bal" + szinek['sárga'] + " szavak, vagy azok kezdőbetűinek a beírásával beírásával működik.")
print("Ha nem tetszik a jelenlegi labirintus, az " + szinek['v_kék'] + "újra" + szinek['sárga'] + " beírásával generálhatsz egy másikat, aminek a méretét is megváltoztathatod.")
print("Ha ki akarsz lépni, akkor ezt az " + szinek['v_kék'] + "exit" + szinek['sárga'] + " beírásával megteheted.")
print("Sok sikert!")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def bevitel():
    global x
    global y

    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

    x = input(szinek['sárga'] + "\nAdd meg a pálya szélességét: ")
    while x.isnumeric() == False:
        x = input(szinek['piros'] + "SZÁMOT adjál meg: ")
    x = int(x) + 2

    y = input(szinek['sárga'] + "Add meg a pálya magasságát: ")
    while y.isnumeric() == False:
        y = input(szinek['piros'] + "SZÁMOT adjál meg: ")
    y = int(y) + 2

x_sor = 0
x_oszlop = 0


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def lab_generalas(x, y):

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


    print()

    for oszlop in range(y):
        for sor in range(x):

            if labirintus[oszlop][sor] == 1:

                #Ez a keretre vonatkozik:
                if oszlop == 0:
                    if sor == 0:
                        print(szinek['sárga'] + "┌", end="")
                    elif sor == (x - 1):
                        print(szinek['sárga'] + "┐", end="")
                    elif labirintus[oszlop + 1][sor] == 1:
                        print(szinek['sárga'] + "┬", end="")
                    else:
                        print(szinek['sárga'] + "─", end="")

                elif oszlop == (y - 1):
                    if sor == 0:
                        print(szinek['sárga'] + "└", end="")
                    elif sor == (x - 1):
                        print(szinek['sárga'] + "┘", end="")
                    elif labirintus[oszlop - 1][sor] == 1:
                        print(szinek['sárga'] + "┴", end="")
                    else:
                        print(szinek['sárga'] + "─", end="")

                elif sor == 0:
                    if labirintus[oszlop][sor + 1] == 1:
                        print(szinek['sárga'] + "├", end="")
                    else:
                        print(szinek['sárga'] + "│", end="")

                elif sor == (x - 1):
                    if labirintus[oszlop][sor - 1] == 1:
                        print(szinek['sárga'] + "┤", end="")
                    else:
                        print(szinek['sárga'] + "│", end="")

                else:

                    #Ez az akadályokra vonatkozik:
                    if labirintus[oszlop][sor - 1] == 1:
                        if labirintus[oszlop][sor + 1] == 1:
                            if labirintus[oszlop - 1][sor] == 1:
                                if labirintus[oszlop + 1][sor] == 1:
                                    print(szinek['sárga'] + "┼", end="")
                                else:
                                    print(szinek['sárga'] + "┴", end="")
                            elif labirintus[oszlop + 1][sor] == 1:
                                print(szinek['sárga'] + "┬", end="")
                            else:
                                print(szinek['sárga'] + "─", end="")
                        elif labirintus[oszlop - 1][sor] == 1:
                            if labirintus[oszlop + 1][sor] == 1:
                                print(szinek['sárga'] + "┤", end="")
                            else:
                                print(szinek['sárga'] + "┘", end="")
                        elif labirintus[oszlop + 1][sor] == 1:
                            print(szinek['sárga'] + "┐", end="")
                        else:
                            print(szinek['sárga'] + "─", end="")
                    elif labirintus[oszlop][sor + 1] == 1:
                        if labirintus[oszlop - 1][sor] == 1:
                            if labirintus[oszlop + 1][sor] == 1:
                                print(szinek['sárga'] + "├", end="")
                            else:
                                print(szinek['sárga'] + "└", end="")
                        elif labirintus[oszlop + 1][sor] == 1:
                            print(szinek['sárga'] + "┌", end="")
                        else:
                            print(szinek['sárga'] + "─", end="")
                    elif labirintus[oszlop - 1][sor] == 1:
                        print(szinek['sárga'] + "│", end="")
                    elif labirintus[oszlop + 1][sor] == 1:
                        print(szinek['sárga'] + "│", end="")
                    else:
                        print(szinek['sárga'] + "┼", end="")
            elif labirintus[oszlop][sor] == 0:
                print(" ", end="")
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

    if mozgas == "fel" or mozgas == "f":
        if labirintus[x_oszlop - 1][x_sor] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop - 1][x_sor] == "◯":
            nyertel()
            run = False
        else:
            labirintus[(x_oszlop - 1)].pop(x_sor)
            labirintus[(x_oszlop - 1)].insert(x_sor, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "le" or mozgas == "l":
        if labirintus[x_oszlop + 1][x_sor] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop + 1][x_sor] == "◯":
            nyertel()
            run = False
        else:
            labirintus[x_oszlop + 1].pop(x_sor)
            labirintus[x_oszlop + 1].insert(x_sor, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "jobb" or mozgas == "j":
        if labirintus[x_oszlop][x_sor + 1] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop][x_sor + 1] == "◯":
            nyertel()
            run = False
        else:
            labirintus[x_oszlop].pop(x_sor + 1)
            labirintus[x_oszlop].insert(x_sor + 1, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "bal" or mozgas == "b":
        if labirintus[x_oszlop][x_sor - 1] == 1:
            print(szinek['piros'] + "Ide nem léphetsz!")
        elif labirintus[x_oszlop][x_sor - 1] == "◯":
            nyertel()
            run = False
        else:
            labirintus[x_oszlop].pop(x_sor - 1)
            labirintus[x_oszlop].insert(x_sor - 1, "X")
            labirintus[x_oszlop].pop(x_sor)
            labirintus[x_oszlop].insert(x_sor, 0)
    elif mozgas == "újra":
        bevitel()
        lab_generalas(x, y)
        rajz()
    elif mozgas == "exit":
        run = False
    else:
        print(szinek['piros'] + "Ez nem egy opció!\n")


def nyertel():
    print(szinek['v_zöld'] + "\n\n\t                                                   /")
    print("\t│\\    │   \\   /  ┌──────  ┌─────┐   ────┬────  ┌──────   │        │")
    print("\t│ \\   │    \\ /   │        │     │       │      │         │        │")
    print("\t│  \\  │     │    ├──────  ├────/        │      ├──────   │        │")
    print("\t│   \\ │     │    │        │     \\       │      │         │        │")
    print("\t│    \\│     │    └──────  │      \\      │      └──────   └──────  .")

print()

bevitel()
lab_generalas(x, y)

run = True
while run:
    rajz()
    irany = (input(szinek['sárga'] + "\nMerre akarsz mozogni? (" + szinek['v_kék'] + "fel" + szinek['sárga'] + ", " + szinek['v_kék'] + "le" + szinek['sárga'] + ", " + szinek['v_kék'] + "jobbra" + szinek['sárga'] + " vagy " + szinek['v_kék'] + "balra" + szinek['sárga'] + "): "))
    move(irany)
