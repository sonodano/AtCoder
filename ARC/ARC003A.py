#%%
N = int(input())
R = input()

A = R.count('A')
B = R.count('B')
C = R.count('C')
D = R.count('D')

ans = 4 * A + 3 * B + 2 * C + 1 * D
ans = ans/N
print(ans)