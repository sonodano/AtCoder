#%%
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temp = [abs(T - h * 0.006 - A) for h in H] # 各地点の気温- 平均温度 の絶対値が最小になるものが、平均値に一番近いはず
ans = temp.index(min(temp)) + 1
print(ans)