#%%
x = input()

x = x.replace('ch', '').replace('o', '').replace('k', '').replace('u', '')
if not x:
    print('YES')
else:
    print('NO')

