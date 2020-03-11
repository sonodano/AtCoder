#%%
import itertools

N = int(input())

m_cnt = 0
a_cnt = 0
r_cnt = 0
c_cnt = 0
h_cnt = 0

for _ in range(N):
    s = input()
    if s[0] == 'M':
        m_cnt += 1
    elif s[0] == 'A':
        a_cnt += 1
    elif s[0] == 'R':
        r_cnt += 1
    elif s[0] == 'C':
        c_cnt += 1
    elif s[0] == 'H':
        h_cnt += 1


ans = 0
march = (m_cnt, a_cnt, r_cnt, c_cnt, h_cnt)
for cb in itertools.combinations(march, 3):
    ans += cb[0] * cb[1] * cb[2]


print(ans)
