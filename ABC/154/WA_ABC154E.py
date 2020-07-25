#%%
# できなかった
H, N = map(int, input().split())

A = []
B = []
diff = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    diff.append(a - b)

count = 0
ans = 0

max_d_idx = diff.index(max(diff))
max_d_a = A[max_d_idx]
max_d_b = B[max_d_idx]
while True:
    if max_d_a * count == H:
        import sys
        ans = count * B[max_d_idx]
        print(ans)
        sys.exit()
    elif max_d_a * count < H < max_d_a * (count + 1):
        break
    count += 1

#%%
ans = (count + 1) * B[max_d_idx]
m_base = count * B[max_d_idx]
for i in range(N):
    n = 1
    while True:
        if max_d_a * count + n * A[i] >= H:
            ans = min(ans, m_base + B[i])
            break
        n += 1
print(ans)

