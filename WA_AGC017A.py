#%%
N, P = map(int, input().split())
A = list(map(int, input().split()))

flag = True
for a in A:
    if a % 2 != 0:
        flag = False

if flag:
    if P == 0:
        ans = 2 ** N
    else:
        ans = 0
else:
    ans = 2 ** (N-1)

print(ans)
#%%
# 当然のように間に合わない
count = 0
def dfs(i, sum):
    global count
    if i == N:
        if sum // 2 == P:
            count += 1
    else:
        dfs(i + 1, sum + A[i]) # 選ぶパターン
        dfs(i + 1, sum)   # 選ばないパターン

dfs(0, 0)
print(count)
