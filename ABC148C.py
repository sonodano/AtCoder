#%%
# atcoderでは最大公約数を求めるgcd()はmathモジュールではなくfractionsモジュールです！！（引っかかった）
# https://note.nkmk.me/atcoder-python-numpy-scipy-version/
A, B = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

ans = lcm(A, B)
print(int(ans))
