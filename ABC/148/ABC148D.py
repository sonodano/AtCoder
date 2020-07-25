#%%
import sys
N = int(input())
a_list = list(map(int, input().split())) #[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 1]

try:
    idx = a_list.index(1)
except:
    print(-1)
    sys.exit(0)

#idx = 0
value = 1

for k, v in enumerate(a_list):
    if idx <= k and value+1 == v:
        value += 1

print(len(a_list) - value)


# try:
#     idx = a_list.index(value)
#     ans += a_list.index(1)
#     a_list = a_list[idx:]
#     value += 1
# except:
#     print(-1)
#     sys.exit(0)
#
# while True:
#     try:
#         idx = a_list.index(value)
#         ans += idx - 1
#         a_list = a_list[idx:]
#         value += 1
#     except:
#         ans += len(a_list) - 1
#         break
#
# print(ans)
#
# # for k, v in enumerate(a_list):
# #     print(k+1, v)

#%%
