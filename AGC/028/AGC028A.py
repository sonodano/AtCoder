#%%
N, M = map(int, input().split())
S = input()
T = input()

#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)
#%%
# L は N, Mの最小公倍数
L = lcm(N, M)

# 文字が一致しなければならないindexは公倍数で、L//MとL//Nが入れ替わる
if S[::L//M] == T[::L//N]:
    print(L)
else:
    print(-1)
