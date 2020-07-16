#%%
N = int(input())
A = list(map(int, input().split()))

#%%
A.sort(reverse=True)
ans = A[0]
res = N - 2
q, m = divmod(res, 2)
for i in range(1, q+1):
    ans += 2 * A[i]
if m != 0:
    ans += A[i+1]

print(ans)
