import sys

input = sys.stdin.readline #sys.stdin.readline()のほうが早いらしい
n = input()
a_list = list(map(int, input().split()))

count = 0
while all(a%2==0 for a in a_list): # sum(a%2 for a in a_list)==0:
    count += 1
    a_list = [a/2 for a in a_list]

print(count)

# このコードだと時間制限に引っかかる
# pypyでもむりぽ…
# list(map())を間違ってただけだった…