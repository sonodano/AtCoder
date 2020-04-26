#%%
import re
s = input()

#%%
# 愚直に実装する方法しか思い浮かばない
users = re.findall('@[a-z]+', s)
users = sorted(set(users))

for u in users:
    print(u[1:])