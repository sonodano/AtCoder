#%% itertoolsを使ったbit全探索
import itertools

# 10個のbit組み合わせ
cnt = 0
for i in itertools.product([0, 1], repeat=10):
    cnt += 1
print(cnt)
# 2^Nと一致する

