# *-* coding: utf-8 *-*

import random
def main():
    skrito_stevilo = random.randint(0, 20)

    while True:
        odgovor = int(raw_input("Ugani skrito število med 1 in 20: "))
        if odgovor == skrito_stevilo:
            print("Pravilno")
            break
        elif odgovor < skrito_stevilo:
            print("Tvoje število je prenizko.")
        elif odgovor > skrito_stevilo:
            print("Tvoje skrito število je previsoko.")
        else:
            print("Napačno")

main()