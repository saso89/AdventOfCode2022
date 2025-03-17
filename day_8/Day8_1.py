# Day 8
# Part 1: število vidnih dreves
# uvoz podatkov, identifikacija spremenljivk
podatki = open("day_8.txt", encoding="utf8").readlines()
mrezaDreves = []
stevecVidnihDreves = 0

# napolnimo listo s podatki (9900 elementov)
for line in podatki:
    mrezaDreves.append(list(line.replace('\n', '')))

# preštejemo drevesa na robu, ki so vsekakor vidna (2 x dolžina prve vrste + 2 x število vrstic - 4 elementi, ki so upoštevani dvakrat) (394 elementov)
stevecVidnihDreves = len(mrezaDreves[0]) * 2 + len(mrezaDreves) * 2 - 4

# pregledamo še ostala drevesa (skrajnih robov ne pregledujemo, v vseh 4 smereh preverjamo, če obstaja višje drevo)
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

            levoVisji, desnoVisji, zgorajVisji, spodajVisji = False, False, False, False

            # če najdemo kakšno drevo, ki je večje od tega na katerem smo (v vseh smereh) potem vrne True drugače False
            levoVisji = any(next((x for x in reversed(vrstaDrevesLevo) if int(x) >= visinaDrevesa), [False]))
            desnoVisji = any(next((x for x in vrstaDrevesDesno if int(x) >= visinaDrevesa), [False]))
            zgorajVisji = any(next((x for x in reversed(stolpecDrevesZgoraj) if int(x) >= visinaDrevesa), [False]))
            spodajVisji = any(next((x for x in stolpecDrevesSpodaj if int(x) >= visinaDrevesa), [False]))

            # če je vsaj en pogoj == False, potem je drevo vidno, zato števcu prišejemo +1
            if levoVisji == False or desnoVisji == False or zgorajVisji == False or spodajVisji == False:
                stevecVidnihDreves += 1

print(stevecVidnihDreves)