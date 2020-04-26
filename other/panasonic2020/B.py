#%%
H, W = map(int, input().split())

#%%
ho = H // 2 + H % 2
he = H // 2
wo = W - (W // 2)
we = W // 2
ans = ho * wo + he * we
if H == 1 or W == 1:
    print(1)
else:
    print(ans)
