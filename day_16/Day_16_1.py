#Day 16
#Part 1
import sys
from functools import cache

@cache
def resitev(pos, time, opened):
    if time == 0:
        return 0

    #hoja po ventilih in iskanje največjega pristika, ki ga lahko sprostimo z odpiranjem ventilov
    rezultat = max(resitev(n, time - 1, opened) for n in mapa[pos])

    #odpiramo samo tiste ventile, kjer je hitrost pretoka večja od 0 in še niso bili odprti
    if pretok[pos] > 0 and pos not in opened:
        #pretvorba v navadni set ker frozenset ne dovoli dodajanja - mutability
        noviset_odprti = set(opened)
        noviset_odprti.add(pos)

        #zmnožimo preostali čas in hitrost pretoka ter rekurzivno kličemo preostale minute. 
        #vrnemo največji rezultat
        rezultat = max(rezultat, (time - 1) * pretok[pos] + resitev(pos, time - 1, frozenset(noviset_odprti)))
    return rezultat

podatki = [line.replace("\n","") for line in open("day_16.txt", encoding="utf8").readlines()]
pretok = {}
mapa = {}

# urejanje podatkov
for line in podatki:
    splittedLine = line.split(" ")
    ventil = splittedLine[1]
    pretok[ventil] = int(splittedLine[4].split("=")[1].strip(";"))
    mapa[ventil] = [t.strip(',') for t in splittedLine[9:]]

print(resitev('AA', 30, frozenset()))