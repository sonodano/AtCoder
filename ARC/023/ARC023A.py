#%%
from math import floor

y = int(input())
m = int(input())
d = int(input())

def prog(y, m ,d):
    if m == 1 or m == 2:
        y -= 1
        m += 12
    days = 365 * y + floor(y/4) - floor(y/100) + floor(y/400)\
           + floor(306 * (m + 1) / 10) + d -429
    return days


end = prog(2014, 5, 17)
print(end - prog(y, m, d))