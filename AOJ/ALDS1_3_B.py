#%%
# pythonだとdequeで簡単に実装できちゃうけど、題意に沿ってない気もする…
# deque使わないで頑張れってことかしら…？
from collections import deque
n, q = map(int, input().split())

que = deque()
for _ in range(n):
    k, v = input().split()
    que.append([k, int(v)])

#%%
p_time = 0
while True:
    k, v = que.popleft() # 先頭にあるプロセスを取り出す
    if v <= q: # プロセス制限時間q以内に終わるならば、そのまま削除してこれまでの実行時間を表示
        p_time += v
        print(k, p_time)
    else: # プロセス制限時間q以内に終わらないときは、再びqueに追加する
        p_time += q
        que.append([k, v-q])

    if len(que) == 0: # すべてのqueがなくなったら終了
        break




