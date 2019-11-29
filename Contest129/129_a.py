# Airplane
import sys
import itertools

input = sys.stdin.readline #sys.stdin.readline()のほうが早いらしい

a_list = list(map(int, input().split()))

combi = list(itertools.combinations(a_list, 2))
sum_list = [sum(i) for i in combi]
print(min(sum_list))