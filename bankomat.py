attempts = 0
pin = "7766"
saldo = 5000
max_attempts = 2


def menu():
    global saldo
    global in_pin

    nav = input("1: Se saldo, 2: Sätt in pengar, 3: Ta ut pengar, 4: Avsluta:  ")

    if nav == "1":
        print("Saldo: " + str(saldo) + " kr")
        menu()

    elif nav == "2":
        saldo += int(input("Hur mycket pengar vill du sätta in: "))
        menu()

    elif nav == "3":
        saldo -= int(input("Hur mycket pengar vill du ta ut: "))
        menu()

    elif nav == "4":
        exit()

    else:
        print(nav + (" är inte ett korrekt komando!"))
        menu()


print("Välkommen till bankomaten!")

while attempts < max_attempts:
    in_pin = input("Pinkod: ")

    if in_pin == pin:
        print("Välkommen in!")
        menu()

    else:
        print("Du har angett fel pinkod")
        attempts += 1

if attempts >= max_attempts:
    print("Du har försökt för många gånger!")