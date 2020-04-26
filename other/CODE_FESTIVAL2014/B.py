#%%
B = input()

even_odd = 'o'
ans = 0
for b in B:
    if even_odd == 'o':
        ans += int(b)
        even_odd = 'e'
    else:
        ans -= int(b)
        even_odd = 'o'

print(ans)
