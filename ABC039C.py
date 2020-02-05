#%%
S = input()

#%%
oct = S[:13]
if oct == 'WBWBWWBWBWBWW':
    print('Do')
elif oct == 'WBWWBWBWBWWBW':
    print('Re')
elif oct == 'WWBWBWBWWBWBW':
    print('Mi')
elif oct == 'WBWBWBWWBWBWW':
    print('Fa')
elif oct == 'WBWBWWBWBWWBW':
    print('So')
elif oct == 'WBWWBWBWWBWBW':
    print('La')
elif oct == 'WWBWBWWBWBWBW':
    print('Si')

#%%
# 賢い解法
S = str(input())
number = [4, 2, 0, 11, 9, 7, 5]
melody = ["Do", "Re", "Mi", "Fa", "So", "La", "Si"]

for i in range(len(S)):
    if S[i:i + 9] == "WWBWBWBWW":  # この時iがMi
        x = number.index(i)
        print(melody[x])