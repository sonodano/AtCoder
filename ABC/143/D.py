#%%
# TODO 要復習
#  a, bを固定する考え方まではあってる。a, bを固定して、ある長さ以上以下のcを求める。配列はソートしてもっておき、二分探索で範囲を求める.O(N2logN)
import bisect
n = int(input())
L = list(map(int, input().split()))
#%%
L.sort()

ans = 0
for i in range(n-2): # aを固定
    for j in range(i+1, n-1): # bを固定
        ab = L[i] + L[j]
        idx = bisect.bisect_left(L, ab, lo=j) # 二分探索でcが取れる値の最大値のindexを取得（bisect_leftで閉区間
        ans += max(idx - (j+1), 0)

print(ans)

# ほかにも尺取り法や累積和を使う方法がある