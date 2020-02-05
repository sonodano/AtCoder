#%%
N, T = map(int, input().split())
t_list = list(map(int, input().split()))

diff_t = [t_list[i+1] - t_list[i] for i in range(N-1)]

ans = 0
for dt in diff_t:
    if dt <= T:
        ans += dt
    else:
        ans += T

ans += T
print(ans)

#%%
# もうちょっと賢いコード（解説通り）
# https://atcoder.jp/contests/arc073/submissions/8340385
n, t = map(int, input().split())
l = list(map(int, input().split()))
c = t
for i in range(n-1):
  c += min(t, l[i+1] - l[i])
print(c)