#%%
from collections import deque
n = int(input())
Cs = input()

#%%
widx = deque()
ridx = deque()
for i in range(n):
    if Cs[i] == 'W':
        widx.append(i)
    else:
        ridx.append(i)
#%%
cnt = 0
while True:
    if len(widx) == 0 or len(ridx) == 0:
        break
    elif widx[0] < ridx[-1]:
        widx.popleft()
        ridx.pop()
        cnt += 1
    else:
        break

print(cnt)



