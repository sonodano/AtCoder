#%%
# 案外TLEしなかった
A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for a in range(A+1):
    tmp_a = X - a * 500
    if tmp_a == 0:
        ans += 1
        continue
    elif tmp_a < 0:
        break
    else:
        for b in range(B+1):
            tmp_b = tmp_a - b * 100
            if tmp_b == 0:
                ans += 1
                continue
            elif tmp_b < 0:
                break
            else:
                for c in range(C+1):
                    tmp_c = tmp_b - c * 50
                    if tmp_c == 0:
                        ans += 1
                        continue
                    elif tmp_b < 0:
                        break

print(ans)

#%%
# もうちょっと素朴でいいかも
ans = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500 * i + 100 * j + 50 * k == X:
                ans += 1
print(ans)