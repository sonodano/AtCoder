#%%
# ABC086A - Product
a, b = map(int, input().split())

if a * b % 2 == 0:
    print("Even")
else:
    print("Odd")

#%%
# ABC081A - Placing Marbles
s1, s2, s3 = map(int, list(input()))
print(s1+s2+s3)

#%%
# ABC081B - Shift only
N = input()
A = list(map(int, input().split()))
cnt = 0
while all(a%2==0 for a in A):
    A = [a/2 for a in A]
    cnt += 1
print(cnt)

#%%
# ABC087B - Coins
a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            x_d = 500 * i + 100 * j + 50 * k
            if x == x_d:
                count += 1

print(count)

#%%
# 	ABC083B - Some Sums
n, a, b = list(map(int, input().split()))

somesums = 0
for i in range(n+1):
    s = sum([int(j) for j in str(i)])
    if a <= s <= b:
        somesums += i

print(somesums)

#%%
# ABC088B - Card Game for Two
n = int(input())
a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

alice = sum(a_list[0::2])
bob = sum(a_list[1::2])

print(alice-bob)

#%%
# ABC085B - Kagami Mochi
N = int(input())

d_list = []
for n in range(N):
    d = int(input())
    d_list.append(d)


d_unique = list(set(d_list))
print(len(d_unique))

#%%
# ABC085C - Otoshidama
import sys
n, t = list(map(int, input().split()))

for i in range(n+1):
    for j in range(n+1-i):
        x, y, z = i, j, n-i-j
        if (10000*x + 5000*y + 1000*z) == t:
            print(x, y, z)
            sys.exit()

# 何もなかった場合
print(-1, -1, -1)

#%%
# ABC049C - 白昼夢 / Daydream

