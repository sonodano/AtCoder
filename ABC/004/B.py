#%%
#field = [list(input().split()) for _ in range(4)]
field = [['.', '.', '.', '.'],
         ['.', 'o', 'o', '.'],
         ['.', 'x', 'x', '.'],
         ['.', '.', '.', '.']]
#%%
for f in reversed(field):
    print(' '.join(f[::-1]))