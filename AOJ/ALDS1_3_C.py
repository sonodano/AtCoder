#%%
# 連結リストも題意に沿ってない気がするけどdequeがあるからいいよね！
from collections import deque
n = int(input())

que = deque()
for _ in range(n):
    cmd = input()

    if cmd == 'deleteFirst':
        try:
            que.popleft()
        except:
            pass
    elif cmd == 'deleteLast':
        try:
            que.pop()
        except:
            pass
    else:
        cmd, x = cmd.split()
        if cmd == 'insert':
            que.appendleft(x)
        elif cmd == 'delete':
            try:
                que.remove(x)
            except:
                pass

print(*que)