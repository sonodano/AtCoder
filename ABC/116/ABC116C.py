#%%
# コードが汚い…
N = int(input())
h_list = list(map(int, input().split()))

ans = 0
h_list.append(0)
while True:
    idx_left = 0
    idx_right = None
    for i in range(N):
        if h_list[i] == 0 and h_list[i+1] != 0:
            idx_left = i+1
        if h_list[i] != 0 and h_list[i+1] == 0:
            idx_right = i+1

        if idx_right is not None:
            if idx_right == idx_left:
                pour = h_list[idx_left]
                ans += pour
                h_list[idx_left] = 0
            else:
                pour = min(h_list[idx_left:idx_right])
                for j in range(idx_right - idx_left):
                    h_list[idx_left+j] = h_list[idx_left+j] - pour
                ans += pour
            break

    if all([h == 0 for h in h_list]):
        break

print(ans)
#%%
# 再帰でやる方法
# https://www.suzu6.net/posts/64-atcoder-bc116/
count = 0

def mizu(h):
    global count
    # 終端処理
    if len(h) is 0:
        return
    if len(h) is 1:
        count = count + h[0]
        return
    # その範囲の最小値
    m = min(h)
    count = count + m
    # 残りの高さ
    h = [i - m for i in h]
    while 0 in h:
        # （最小値だった）0の箇所で分割
        mizu(h[:h.index(0)])
        h = h[h.index(0)+1:]
    mizu(h)

N = int(input())
h = list(map(int, input().split()))
mizu(h)
print(count)

#%%
# なんかめっちゃ短い
# https://atcoder.jp/contests/abc116/submissions/9351031
N=int(input())
H=list(map(int,input().split()))
cnt=0
for i in range(N-1):
  cnt+=min(H[i],H[i+1])
print(sum(H)-cnt)