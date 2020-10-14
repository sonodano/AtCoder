#%%
n, q = map(int, input().split())
S = input()

#%%
ac = [0] * n
cnt = 0
for i in range(n-1):
    if S[i] == 'A' and S[i+1] == 'C':
        cnt += 1
    ac[i+1] = cnt

#%%
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ans = ac[r] - ac[l]

    print(ans)