#%%
N, A, B = map(int, input().split())

p1 = 10e18
p2 = 10e18
p3 = 10e18
p4 = 10e18
p5 = 10e18

if (B - A) % 2 == 0:
    p1 = (B - A) // 2
else:
    p2 = B - 1 #左端による
    p3 = N - A # 右端による
    # Aを1回左端に寄せてから、折り返し
    p4 = (B - A) // 2 + A
    # Bを1回右端に寄せてから折り返し
    p5 = (-A + B -1) //2 + N -B + 1

print(min(p1, p2, p3, p4, p5))