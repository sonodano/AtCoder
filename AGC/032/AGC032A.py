#%%
n = int(input())
b = list(map(int, input().split()))

# 生成されたBの逆順からとっていく
# b[i] = jになる一番後ろの値からpopしていき、最後に逆順にすれば答え
ans = []
while True:
    flag = False
    if len(b) == 0: # 場合分けがちょっと冗長感ある
        break

    for i in range(len(b)):
        if i+1 == b[i]:
            idx = i
            flag = True
    if flag:
        tmp = b.pop(idx)
        ans.append(tmp)
    else:
        ans = [-1]
        break

print('\n'.join(map(str, reversed(ans))))
