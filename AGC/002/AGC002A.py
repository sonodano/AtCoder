#%%
a, b = map(int, input().split())

if a > 0 and b > 0:
    print('Positive')
elif a <=0 and 0 <= b:
    print('Zero')
else:
    diff = b - a + 1
    if diff % 2 == 0:
        print('Positive')
    else:
        print('Negative')