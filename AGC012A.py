#%%
N = int(input())
a_list = list(map(int, input().split()))

a_list.sort(reverse=True)
ans = sum(a_list[1:2*N:2])
print(ans)

#%% md
'''
解法: 
10 9 8 7 6 5 4 3 2
があったとき最大となるのは、
10-9-?
8-7-?
6-5-?
の組なので、大きい順にペアを作った後、小さい方の値を足し合わせればよい
'''
