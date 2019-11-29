# Balance
n = input()
w_list = list(map(int, input().split()))

delta = float('inf')
for i in range(len(w_list)):
    ret = abs(sum(w_list[:i])-sum(w_list[i:]))
    if ret < delta:
        delta = ret

print(delta)