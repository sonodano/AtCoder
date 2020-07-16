#%%
n = int(input())
A = list(map(int, input().split()))

#%%
A = [0] + A
A.append(0)
#%%
diff = [abs(A[i] - A[i+1]) for i in range(len(A)-1)]
diff2 = [abs(A[i] - A[i+2]) for i in range(len(A)-2)]
total = sum(diff)

for i in range(n):
    ans = total - sum(diff[i:i+2]) + diff2[i]
    print(ans)
