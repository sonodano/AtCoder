#%%
n, k, s = map(int, input().split())

#%%
billion = 1000000000

if s == billion:
    front = [s] * k
    back = [1] * (n - k)
else:
    front = [s] * k
    back = [s+1] * (n - k)

front.extend(back)
print(*front)
# print(*front, *back) # python3.4だと使えない！？