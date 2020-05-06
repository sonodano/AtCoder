#%%
formula = input().split()

ans = []
for f in formula:
    if f == '+':
        a = ans.pop()
        b = ans.pop()
        ans.append(a + b)
    elif f == '-':
        a = ans.pop()
        b = ans.pop()
        ans.append(b - a)
    elif f == '*':
        a = ans.pop()
        b = ans.pop()
        ans.append(b * a)
    else:
        ans.append(int(f))

print(*ans)