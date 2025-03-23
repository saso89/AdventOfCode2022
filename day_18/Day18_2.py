#Day 18:
#Part 2:
import numpy as np
from collections import deque

# Breadth First Search - iskanje v širino
def vidnoOdZunaj(x,y,z,c):
    queue = deque()
    queue.append((x, y, z))
    obiskano = set()

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in obiskano:
            continue
        obiskano.add((x, y, z))
        if x < 0 or x > 24 or y < 0 or y > 24 or z < 0 or z > 24:
            return True
        if c[x,y,z] == '#':
            continue
        for dx, dy, dz in koordinateSoseda:
            queue.append((x+dx, y+dy, z+dz))
    return False

#kocko napolnemo s pikami
podatki = [line.replace("\n", "") for line in open("day_18.txt", encoding="utf8").readlines()]
kocka = np.full((25, 25, 25), '.', dtype=str)
koordinateSoseda = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

#dobljene koordinate iz podatkov nastavimo kot #
for line in podatki:
    x, y, z = map(int, line.split(','))
    kocka[x,y,z] = '#'

vidne_strani = 0

for x in range(25):
    for y in range(25):
        for z in range(25):
            if kocka[x, y, z] == '#':
                for dx,dy,dz in koordinateSoseda:
                    #preverimo če pridemo do zunanjega roba
                    if vidnoOdZunaj(x+dx,y+dy,z+dz,kocka): vidne_strani += 1

print(vidne_strani)
