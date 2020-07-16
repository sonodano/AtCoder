#%%
n = int(input())
A = list(map(int, input().split()))

#%%
hai = 0
cha = 0
midori = 0
mizu = 0
ao = 0
ki = 0
dai = 0
aka = 0
above = 0
for a in A:
    if 1 <= a <= 399:
        hai = 1
    elif 400 <= a <= 799:
        cha = 1
    elif 800 <= a <= 1199:
        midori = 1
    elif 1200 <= a <= 1599:
        mizu = 1
    elif 1600 <= a <= 1999:
        ao = 1
    elif 2000 <= a <= 2399:
        ki = 1
    elif 2400 <= a <= 2799:
        dai = 1
    elif 2800 <= a <= 3199:
        aka = 1
    else:
        above += 1

n_rate = 8
total = hai + cha + midori + mizu + ao + ki + dai + aka

if total != 0:
    ans_min = total
else:
    ans_min = 1

# TODO 問題文が読めてないパターンでした。3200以上の色は「なんでもよい」
# ans_max = min(n_rate, total+above)
ans_max = total + above
print(ans_min, ans_max)