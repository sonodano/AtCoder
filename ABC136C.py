import sys

n = int(input())
heights = list(map(int, input().split()))

for i in range(len(heights) - 1):
    if (heights[i] < heights[i+1]) and heights[i+1] != 1:
        heights[i+1] += -1
    if heights[i] > heights[i+1]:
        print('No')
        sys.exit(0)

print('Yes')