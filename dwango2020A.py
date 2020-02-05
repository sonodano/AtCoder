#%%
N = int(input())

s_list = []
t_list = []
for _ in range(N):
    s, t = input().split()
    s_list.append(s)
    t_list.append(int(t))

X = input()


idx = s_list.index(X)
ans = sum(t_list[idx+1:])
print(ans)

