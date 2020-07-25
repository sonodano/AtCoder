#%%
N = int(input())
S, T = map(str, input().split())

ans = ''.join(s+t for s, t in zip(S, T))
print(ans)