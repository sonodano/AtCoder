#%%
import numpy as np
K, N = map(int, input().split())
Al = list(map(int, input().split()))

diff = np.diff(Al)
diff = np.append(diff, K-Al[-1]+Al[0])

ans = K - diff.max()
print(int(ans))
