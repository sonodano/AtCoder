#%%
# 辛抱強く地道に全パターン試しましょう
s = list(input())
k = int(input())

def count_replace(l):
    ret = 0
    cnt = 1
    for i in range(len(l)-1):
        if l[i] == l[i+1]: #
            cnt += 1
        elif l[i] != l[i+1]:
            ret += cnt//2
            cnt = 1
    ret += cnt // 2 # 最後尾（ループが尽きた）のための処理. 末尾が連続していた場合には連続分が追加、それ以外は0が追加
    return ret

if len(set(s)) == 1: # すべての文字が同じとき
    ans = (len(s) * k) // 2
elif s[0] != s[-1]: #先頭末尾が一致しないとき
    ans = count_replace(s)
    ans = k * ans
else: # 先頭末尾が一致
    # 先頭の連続する文字数
    cnt_pre = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt_pre += 1
        else:
            break
    # 末尾の連続する文字数
    cnt_pos = 1
    for i in reversed(range(len(s))):
        if s[i] == s[i-1]:
            cnt_pos += 1
        else:
            break
    # 先頭の連続数//2+末尾の連続数//2＋(k-1)*（先頭+末尾）の連続数//2
    ans = cnt_pre//2 + cnt_pos//2 + (k-1) * ((cnt_pos+cnt_pre)//2)
    # 先頭、末尾以外の部分のカウント
    ret = count_replace(s[cnt_pre:-cnt_pos])
    ans += k * ret

print(ans)
