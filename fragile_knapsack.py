file = open('vstup4.txt', 'r')
filecontent = file.read().splitlines()
file.close()

# nacitanie klucovych premennych zo suboru
N = int(filecontent[0])
W = int(filecontent[1])
F_max = int(filecontent[2])

all_items = []
for i in range(3, len(filecontent)):
    line = filecontent[i].split(' ')
    item = []
    for item_info in line:
        item.append(int(item_info))
    all_items.append(item)

print('\nPocet vstupujucich predmetov', N)
print('\nVaha ruksaku', W)
print('\nMaximalny pocet krehkych predmetov v ruksaku', F_max)

print('\nPredmety')
print(' n| p| w| f')
for r in all_items:
    print(r)

print('\n')

# incializacia potrebneho 3d pola - N riadkov, W stlpcov, F_max + 1 velkost pola na pozicii [x][y]
V = [[[0 for x in range(F_max + 1)] for x in range(W + 1)] for x in range(N + 1)]

# Pustenie algoritmu na 3d poli
for i in range(1, N + 1):
    for w in range(1, W + 1):
        for f in range(F_max + 1):
            # Predmet zatial nevchadza alebo posun na poli "krehkosti"
            if all_items[i - 1][2] > w or all_items[i - 1][3] > f:
                V[i][w][f] = V[i - 1][w][f]
            else:
                # Vzorec
                V[i][w][f] = max(V[i - 1][w][f],
                                 V[i - 1][w - all_items[i - 1][2]][f - all_items[i - 1][3]] + all_items[i - 1][1])

w = W
f = F_max
knap_items = []

# ktore predmety boli do ruksaka pridane
for i in range(N, 0, -1):
    if V[i][w][f] != V[i - 1][w][f]:
        w -= all_items[i - 1][2]
        f -= all_items[i - 1][3]
        knap_items.append(all_items[i - 1])

print('Vysledna matica')
for row in V:
    print(row)

f = open('out.txt', "w")

f.write(str(V[N][W][F_max]) + '\n')
f.write(str(len(knap_items)) + '\n')

for item in sorted(knap_items, key=lambda x: x[0]):
    f.write(str(item[0]) + '\n')

f.close()
print(knap_items)
