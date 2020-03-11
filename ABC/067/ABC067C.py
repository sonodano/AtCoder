#%%
# TODO できなかった
# 総和をXとすると, xiを引いた残りはyi=X-xi. したがって|yi-xi| = |X-2xi|
# xiをすべての場合試せば良い
n = int(input())
a_l = list(map(int, input().split()))

ans = float('inf')
x = 0
X = sum(a_l)
for a in a_l[:-1]:
    x += a
    ans = min(ans, abs(X - 2*x))

print(ans)