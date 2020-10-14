n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#%%
husoku = [a-b for a, b in zip(A, B) if a-b < 0]
amari = [a-b for a, b in zip(A, B) if a-b > 0]
amari.sort(reverse=True)

H = abs(sum(husoku))
if len(husoku) == 0:
    ans = 0
elif H > sum(amari):
    ans = -1
else:
    for i, a in enumerate(amari, start=1):
        H -= a
        if H <= 0:
            ans = len(husoku) + i
            break

print(ans)