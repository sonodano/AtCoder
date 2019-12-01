input()
ps = list(map(int, input().split()))

count = 0
for i in range(len(ps) - 2):
    if (ps[i] < ps[i + 1] < ps[i + 2]) or (ps[i] > ps[i+1] > ps[i+2]):
        count += 1

print(count)