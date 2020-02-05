#%%
n = int(input())
a = list(map(int, input().split()))


a_odd = a[::2]
a_even = a[1::2]

if n % 2 == 0:
    ans = a_even[::-1]
    ans.extend(a_odd)
else:
    ans = a_odd[::-1]
    ans.extend(a_even)

print(*ans)