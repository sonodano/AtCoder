#%%
X = int(input())
A = int(input())
B = int(input())

X = X - A
r = X // B
X = X - B * r
print(X)