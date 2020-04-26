#%%
N = int(input())

mousho = 0
manatsu = 0
natubi = 0
nettaiya = 0
huyubi = 0
mahuyubi = 0

for _ in range(N):
    MaxT, minT = map(float, input().split())
    if MaxT >= 35:
        mousho += 1
    if 35 > MaxT >= 30:
        manatsu += 1
    if 30 > MaxT >= 25:
        natubi += 1
    if minT >= 25:
        nettaiya += 1
    if minT < 0 and MaxT >= 0:
        huyubi += 1
    if MaxT < 0:
        mahuyubi += 1

print(mousho, manatsu, natubi, nettaiya, huyubi, mahuyubi)