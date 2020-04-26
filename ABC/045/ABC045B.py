#%%
from collections import deque
Sa = deque(input())
Sb = deque(input())
Sc = deque(input())

#%%
turn = 'a'
while True:
    if turn == 'a':
        if len(Sa) == 0:
            ans = 'A'
            break
        turn = Sa.popleft()
    elif turn == 'b':
        if len(Sb) == 0:
            ans = 'B'
            break
        turn = Sb.popleft()
    else:
        if len(Sc) == 0:
            ans = 'C'
            break
        turn = Sc.popleft()

print(ans)
