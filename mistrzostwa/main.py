import random
import time

#print(input("podaj imię dla papugi:  ") + " ...hmm... " + teksty[random.randint(0, 5)])
drużyna1 = input("podaj nazwe pierwszej drużyny:  ")
drużyna2 = input("podaj nazwe drugiej drużyny:  ")
czy_mozliwy_remis = input("czy ten mecz może zakończyć się remisem? [t/n]: ")
czy_remis = True
if czy_mozliwy_remis == "n":
    czy_remis = False

print("to zaczynamy mecz pomiędzy: " + drużyna1 + " a " + drużyna2)

for i in range(3):
    print(".")
    time.sleep(1)

drużyna1_gole = (random.randint(0, 5))
drużyna2_gole = (random.randint(0, 5))

if (czy_remis is False) and (drużyna1_gole == drużyna2_gole):
    print("wynik meczu: " + drużyna1 + " " + str(drużyna1_gole) + " : " + drużyna2 + " " + str(drużyna2_gole))
    print("na dogrywkę zapraszamy po przerwie")
    for i in range(3):
        print(".")
        time.sleep(1)
    print("zapraszamy na dogrywkę")
    drużyna1_gole += (random.randint(0, 3))
    drużyna2_gole += (random.randint(0, 3))

if drużyna1_gole == drużyna2_gole:
    print("wynik meczu po dogrywce: " + drużyna1 + " " + str(drużyna1_gole) + " : " + drużyna2 + " " + str(drużyna2_gole))
    print("na rzuty karne zapraszamy po przerwie")
    for i in range(3):
        print(".")
        time.sleep(2)
    print("zapraszamy na rzuty karne")
    drużyna1_gole = 0
    drużyna2_gole = 0
    seria = 1
    while True:
        time.sleep(2)
        drużyna1_karny = (random.randint(0, 1))
        if drużyna1_karny == 1:
            print(drużyna1 + " goooooooooooooooooool!!!!")
        else:
            print(drużyna1 + " pudło")
        time.sleep(2)
        drużyna2_karny = (random.randint(0, 1))
        if drużyna2_karny == 1:
            print(drużyna2 + " goooooooooooooooooool!!!!")
        else:
            print(drużyna2 + " pudło")
        time.sleep(2)
        drużyna1_gole += drużyna1_karny
        drużyna2_gole += drużyna2_karny
        print("wynik po serii " + str(seria) + ": " + drużyna1 + " " + str(drużyna1_gole) + " : " + drużyna2 + " " + str(drużyna2_gole))
        seria += 1
        if (drużyna1_gole != drużyna2_gole) and (seria > 5):
            break

print("wynik meczu: " + drużyna1 + " " + str(drużyna1_gole) + " : " + drużyna2 + " " + str(drużyna2_gole))
komentarze = ["spoko meczyk", "grali jak łajzy", "sędzia kalosz znów źle zasędziował", "ale nuuuda", "moja babcia gra lepiej", "super wrażenia"]
print("komentarze pomeczowe: " + komentarze[random.randint(0, 5)])