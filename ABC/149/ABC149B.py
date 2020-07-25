#%%
import sys
A, B, K = map(int, input().split())

if A + B <= K:
    print(0, 0)
    sys.exit(0)
if A >= K:
    print(A-K, B)
    sys.exit(0)

print(0, A+B-K)