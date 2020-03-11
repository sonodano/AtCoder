#%%
import math
N = int(input())
A = list(map(int, input().split()))


nobug = A.count(0)

ans = sum(A) / (N - nobug)
ans = math.ceil(ans)
print(ans)