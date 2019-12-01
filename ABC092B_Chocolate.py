N = int(input())
d, x = map(int, input().split())

count = 0
for n in range(N):
    participant = int(input())
    count += len(list(range(0, d, participant)))

print(count+x)