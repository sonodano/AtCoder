#%%
S = input()

a = S.count('a')
b = S.count('b')
c = S.count('c')

if max(abs(a - b), abs(b - c), abs(c - a)) >= 2:
    print('NO')
else:
    print('YES')