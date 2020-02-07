#%%
H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

#%%

def get_field(i, j):
    try:
        ret = field[i][j]
    except:
        ret = '.'
    return ret

ans = True
for i in range(H):
    for j in range(W):
        if field[i][j] == '#':
            up = get_field(i-1, j)
            down = get_field(i+1, j)
            left = get_field(i, j-1)
            right = get_field(i, j+1)
            if up == '#' or down == '#' or left == '#' or right == '#':
                ans = True
            else:
                ans = False
                break
    if ans == False:
        break

if ans:
    print('Yes')
else:
    print('No')