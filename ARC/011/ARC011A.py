#%%
m, n, N = map(int, input().split())

ans = N
rest = 0
while True:
    recycle = N//m * n
    rest += N - N//m * m

    if rest >= m:
        recycle += n
        rest -= m

    if recycle == 0:
        break

    ans += recycle
    N = recycle

print(ans)

#%%
''' 別解
m,n,N=map(int,input().split())
a=x=N
while x>=m:
  a+=n*(x//m)
  x=x%m+n*(x//m)
print(a)
'''