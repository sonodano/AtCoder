n, a, b = list(map(int, input().split()))

somesums = 0
for i in range(n+1):
    s = sum([int(j) for j in str(i)])
    if a <= s and s <= b: # a <= s <= bでかけるらしい
        somesums += i

print(somesums)