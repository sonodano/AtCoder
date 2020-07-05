#%%
n = int(input())
ans = n * (n-1)//2 #TODO int(n*(n-1)/2)はダメ（桁数が大きくなるとfloatの精度が怪しい. 確実にintになる//を使うべし）
print(ans)