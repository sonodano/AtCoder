s = str(input())
choices = ['dream', 'dreamer', 'erase', 'eraser']

s = s[::-1]
choices = [rev[::-1] for rev in choices]

while True:
    judge = sum([s.startswith(c) * len(c) for c in choices])
    s = s[judge:]
    if judge == 0:
        break

if len(s) == 0:
    print('YES')
else:
    print('NO')



