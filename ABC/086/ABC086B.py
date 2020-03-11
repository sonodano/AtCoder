#%%
a, b = input().split()
ab = int(a+b)

if int(ab**0.5)**2 == ab:
    # (ab**0.5).is_integer()の方が賢い
    print('Yes')
else:
    print('No')
