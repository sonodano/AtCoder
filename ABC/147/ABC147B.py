#%%
S = str(input())

s_front = S[:len(S)//2]
s_rear = S[len(S)//2:]
if len(s_front) != len(s_rear):
    s_front = s_front + s_rear[0]
s_front = s_front[::-1]

count = 0
for i, j in zip(s_front, s_rear):
    if i != j:
        count += 1

print(count)

