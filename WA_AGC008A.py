#%%
# 何が間違ってるかわかんね…
x, y = map(int, input().split())
l = []
if x <= y:
    l.append(y - x)
if -x <= y: # 最初に1回符号反転
    l.append(y + x + 1)
if x <= -y: # 最後に1回符号反転
    l.append(-y - x + 1)
if -x <= -y: # 両方符号反転
    l.append(-y + x + 2)

ans = min(l)
print(ans)