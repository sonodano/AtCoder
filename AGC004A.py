#%%
import sys
A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 ==0:
    print(0)
    sys.exit(0)

ans = min(B*C, C*A, A*B)
print(ans)