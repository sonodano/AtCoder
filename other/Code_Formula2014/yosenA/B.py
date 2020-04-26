#%%
import re
_ = input()
ps = list(input().split())
qs = list(input().split())


ans = '7 8 9 0\n' \
      ' 4 5 6\n' \
      '  2 3\n' \
      '   1'

for p in ps:
    ans = ans.replace(p, '.')

for q in qs:
    ans = ans.replace(q, 'o')

print(re.sub('[0-9]', 'x', ans))

