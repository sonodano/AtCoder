# 10進数をn進数に変換
# Ref. http://iatlex.com/python/base_change

def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)


def base_n_to10(X, n):
    X = str(X)
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out