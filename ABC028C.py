#%%
import itertools

num = list(map(int, input().split()))

sum_list = [sum(i) for i in itertools.combinations(num, 3)]
sum_list.sort(reverse=True)

print(sum_list[2])