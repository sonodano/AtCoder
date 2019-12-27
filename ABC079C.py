#%%
A, B, C, D = map(int, list(input()))


import operator, itertools, sys

ops = {
    '+': operator.add,
    '-': operator.sub
}
ans = ops['-'](ops['+'](ops['-'](A, B), C), D)

for keys in itertools.product(ops, repeat=3):
    total = ops[keys[2]](ops[keys[1]](ops[keys[0]](A, B), C), D)
    if total == 7:
        ans = '{a}{op1}{b}{op2}{c}{op3}{d}=7'.format(a=A, op1=keys[0], b=B, op2=keys[1], c=C, op3=keys[2], d=D)
        print(ans)
        sys.exit(0)

#%%
# eval()を使えば良かったね
import itertools
A, B, C, D = list(input())
for ops in itertools.product(['+', '-'], repeat=3):
    eq = A + ops[0] + B + ops[1] + C + ops[2] + D
    x = eval(eq)
    if x == 7:
        ans = eq + '=7'
        print(ans)
        break
