A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


dishes = [A, B, C, D, E]
tens = 0
ones = 10
muda = 10
for d in dishes:
    if d % 10 == 0:
        tens += d // 10
    else:
        tens += d // 10 + 1
        if d % 10 < ones:
            muda = d
            ones = d % 10

#%%
if muda % 10 == 0:
    ans = tens * 10
else:
    ans = tens * 10 - (10 - muda % 10)
print(ans)