#%%

N =int(input())
a_list = list(map(int, input().split()))

split = N//2
right = a_list[:split]
left = a_list[split:]

while True:
    if right == left:
        print(0)
    elif right < left:



