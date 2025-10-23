import random


optionen = ["Stein", "Papier", "Schere"]


while True:
    try:
        user_num = int(input("1: Stein, 2: Papier, 3: Schere    : "))
        if 1 <= user_num <= 3:
            break
        else:
            print("wähle eine Zahl zwischen 1 und 3.")
    except ValueError:
        print("bitte entweder 1, 2 oder 3 eingeben")

# Computer wählt zufällig
computer_wahl_num = random.randint(1, 3)

# Wahlen in Text umwandeln
user_wahl_text = optionen[user_num - 1]
computer_wahl_text = optionen[computer_wahl_num - 1]

print(f"\nDu hast:             {user_wahl_text}")
print(f"Der Computer hat:    {computer_wahl_text}\n")

# Gewinner ermitteln
if user_wahl_text == computer_wahl_text:
    print("Unentschieden!")
elif (user_wahl_text == "Stein" and computer_wahl_text == "Schere") or \
     (user_wahl_text == "Schere" and computer_wahl_text == "Papier") or \
     (user_wahl_text == "Papier" and computer_wahl_text == "Stein"):
    print("Du gewinnst!")
else:       
    print("Du verlierst!")
