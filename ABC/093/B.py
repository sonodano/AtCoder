#%%
a, b, k = map(int, input().split())
#%%
a_s = set(list(range(a, min(b+1, a+k))))
b_s = set(list(range(max(a, b-k+1), b+1)))
s_uni = b_s | a_s
print(*sorted(s_uni), sep='\n')