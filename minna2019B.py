#%%
machi = [0, 0, 0, 0]
for _ in range(3):
    a, b = map(int, input().split())
    machi[a-1] += 1
    machi[b-1] += 1

for m in machi:
    if m == 3:
        import sys
        print('NO')
        sys.exit()

print('YES')