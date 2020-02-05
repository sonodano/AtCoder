#%%
C = input()


alpha = [chr(i) for i in range(97, 97+26)]
idx = alpha.index(C)
print(alpha[idx+1])