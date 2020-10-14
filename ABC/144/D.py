#%%
import math

a, b, x = map(int, input().split())

#%%
if x <= 0.5 * a**2 * b:
    phi = math.degrees(math.atan(2*x/a/b/b))
    print(90-phi)
else:
    phi = math.degrees(math.atan(2 * (a**2 * b - x)/a**3))
    print(phi)
