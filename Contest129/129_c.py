# typical stairs
n, m = list(map(int, input().split()))

a_list = []
impossible = False
for _ in range(m):
    _a = int(input())
    if a_list[-1] == _a:
        impossible = True
    a_list.append(int(input()))

if impossible:
    print(0)
else:
