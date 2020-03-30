#%%
import math

N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
#%%
neck = min([A, B, C, D, E])
total = 4 + math.ceil(N/neck)

print(total)