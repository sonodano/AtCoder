import itertools
N = int(input())

coords = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for c1, c2 in itertools.combinations(coords, r=2):
    l2 = (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2
    ans = max(ans, l2)

print(ans**0.5)

