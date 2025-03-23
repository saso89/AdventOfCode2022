#Day 18:
#Part 1:
import numpy as np

#kocko napolnemo s pikami
podatki = [line.replace("\n","") for line in open("day_18.txt", encoding="utf8").readlines()]
kocka = np.full((25,25,25), '.', dtype=str)

#dobljene koordinate iz podatkov nastavimo kot #
for line in podatki:
    x, y, z = map(int, line.split(','))
    kocka[x,y,z] = '#'

vidne_strani = 0

#iteriramo po vseh elementih, najdemo sosede in preverimo, kateri so pika
for x in range(25):
    for y in range(25):
        for z in range(25):
            if kocka[x, y, z] == '#':
                sosedje = [
                    kocka[x - 1, y, z],
                    kocka[x + 1, y, z],
                    kocka[x, y - 1, z],
                    kocka[x, y + 1, z],
                    kocka[x, y, z - 1],
                    kocka[x, y, z + 1]
                ]
                vidne_strani += sosedje.count('.')

print(vidne_strani)