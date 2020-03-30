#%%
x = int(input())

n_gohyaku = x // 500
x -= n_gohyaku * 500
n_goen = x // 5
print(n_gohyaku*1000 + n_goen * 5)
