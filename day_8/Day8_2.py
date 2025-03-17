# Day 8
# Part 2: najvišja scenska ocena / najboljši pogled
# uvoz podatkov, identifikacija spremenljivk
podatki = open("day_8.txt", encoding="utf8").readlines()
mrezaDreves = []
najvisjaOcena = 0

# napolnimo listo s podatki
for line in podatki:
    mrezaDreves.append(list(line.replace('\n', '')))

# pregledamo vsa drevesa (skrajnih robov ne pregledujemo)
for i in range(len(mrezaDreves[0])):
    for j in range(len(mrezaDreves)):
        if i != 0 and i != len(mrezaDreves)-1 and j != 0 and j != len(mrezaDreves[0])-1:
            visinaDrevesa = int(mrezaDreves[i][j])

            vrstaDreves = mrezaDreves[i].copy()
            vrstaDrevesLevo = vrstaDreves[:j]
            vrstaDrevesDesno = vrstaDreves[j+1:]

            stolpecDreves = []
            for k in range(len(mrezaDreves)):
                stolpecDreves.append(mrezaDreves[k][j])
            stolpecDrevesZgoraj = stolpecDreves[:i]
            stolpecDrevesSpodaj = stolpecDreves[i+1:]

            steviloVidnihLevo, steviloVidnihDesno, steviloVidnihZgoraj, steviloVidnihSpodaj = 0, 0, 0, 0

            # levo in gor pregledujemo vzvratno
            for e in reversed(vrstaDrevesLevo):
                steviloVidnihLevo += 1
                if int(e) >= visinaDrevesa:
                    break
            for e in vrstaDrevesDesno:
                steviloVidnihDesno += 1
                if int(e) >= visinaDrevesa:
                    break
            for e in reversed(stolpecDrevesZgoraj):
                if int(e) >= visinaDrevesa:
                    steviloVidnihZgoraj += 1
                    break
                steviloVidnihZgoraj += 1
            for e in stolpecDrevesSpodaj:
                steviloVidnihSpodaj += 1
                if int(e) >= visinaDrevesa:
                    break

            ocena = steviloVidnihLevo * steviloVidnihDesno * steviloVidnihZgoraj * steviloVidnihSpodaj
            if ocena > najvisjaOcena:
                najvisjaOcena = ocena

print(najvisjaOcena)