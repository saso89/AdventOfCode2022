#Day 12:
#Part 1
from collections import deque
podatki = open("day_12.txt", encoding="utf8").readlines()
mreza = []

# preberemo in shranimo v seznam (matrika)
for line in podatki:
    mreza.append(list(line.replace('\n', '')))

# začetni položaj je a - najnižja višina in trenutni položaj (S)
# končni položaj z najboljšim signalom (E) je z - najvišja višina
for i, row in enumerate(mreza):
    for j, item in enumerate(row):
        if item == "S":
            sx = i
            sy = j
            mreza[i][j] = "a"
        if item == "E":
            ex = i
            ey = j
            mreza[i][j] = "z"

# definiramo vrsto in vanjo dodamo začetno koordinato
q = deque()
q.append((0, sx, sy))

visited = {(sx, sy)}

#dijkstra
while q:
    distance, x1, y1 = q.popleft()
    for x2, y2 in [(x1 + 1, y1), (x1 - 1, y1), (x1, y1 + 1), (x1, y1 - 1)]:
        if x2 < 0 or y2 < 0 or x2 >= len(mreza) or y2 >= len(mreza[0]):
            continue
        if (x2, y2) in visited:
            continue
        if ord(mreza[x2][y2]) - ord(mreza[x1][y1]) > 1:
            continue
        if x2 == ex and y2 == ey:
            print(distance + 1)
            exit(0)
        visited.add((x2, y2))
        q.append((distance + 1, x2, y2))