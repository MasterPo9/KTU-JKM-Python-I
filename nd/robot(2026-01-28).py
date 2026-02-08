veiksmai_energija = ["UP", "LEFT", "RIGHT"]
veiksmai_be_energijos = ["WAIT"]
energija = 8
kiek_lauke = 0
veiksmu_skaicius = 0
line = 1

with open("robotas.txt") as f:
    text = f.read().splitlines()

for i in text:

    if i in veiksmai_energija or i in veiksmai_be_energijos:
        if i in veiksmai_energija:
            energija -= 1
        elif i in veiksmai_be_energijos:
            kiek_lauke += 1

        veiksmu_skaicius += 1

        if energija == 0:
            break
    else:
        print(f"Veiksmas \"{i}\" yra netinkamas. (line {line})")
    line += 1

print(f"Atlikti {veiksmu_skaicius} veiksmai.\nRobotas laukė {kiek_lauke} kartus.\nLiko {energija} energijos.")

# Parašyta moodle užduotyje lyg būtų labai sunku, bet ištikro yra visai lengva ^-^
