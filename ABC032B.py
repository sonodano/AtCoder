#%%
# pypyよりpythonの方が10倍ぐらい実行速度速い
s = input()
k = int(input())

pw = []
for i in range(len(s) - k + 1):
    pw.append(s[i:i+k])

ans = len(set(pw))
print(ans)