#%%
H, W = map(int, input().split())

a_list = [input() for _ in range(H)]

print((W+2)*'#')
for a in a_list:
    print('#' + a + '#')

print((W+2)*'#')

