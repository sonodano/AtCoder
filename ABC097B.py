#%%
import sys
X = int(input())

if X == 1:
    print(1)
    sys.exit(0)

ans = 0
for b in range(1, 31+1):
    for p in range(2, 31+1):
        bp = b**p
        if ans <= bp and bp <= X:
            ans = bp

print(ans)
