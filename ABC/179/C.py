#%%
import math
N = int(input())

cnt = 0
same = 0
for n in range(1, N):
    for a in range(1, n):
        b = 1
        while True:
            if a * b < n:
                if a == b:
                    same += 1
                print(a, b, a*b, n)
                cnt += 1
                b += 1

            else:
                break

print(cnt-same)