H, N = map(int, input().split())
a_list = list(map(int, input().split()))

if sum(a_list) >= H:
    print('Yes')
else:
    print('No')