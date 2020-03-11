#%%
N, M = map(int, input().split())

import sys
num = ['9' for _ in range(N)]

# 問答無用でゼロ
if M == 0 and N == 1:
    print(0)
    sys.exit()
#%%
for _ in range(M):
    s, c = map(int, input().split())
    # indexをゼロ始まり
    s -= 1
    # 先頭が0は絶対にだめ
    if s == 0  and c == 0 and N != 1:
        print(-1)
        sys.exit()

    # 重複して同じ値じゃないときはだめ
    if num[s] != '9' and num[s] != c:
        print(-1)
        sys.exit()
    else:
        num[s] = c
#%%
# 先頭に値が入れられなかったときは1で埋める
if num[0] == '9':
    num[0] = 1
# 他のところはゼロで埋める
for i in range(N):
    if num[i] == '9':
        num[i] = 0

ans = int(''.join(map(str, num)))
print(ans)


