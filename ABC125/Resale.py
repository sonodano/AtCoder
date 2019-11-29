n = int(input())
v_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

#n = 4
#v_list = [13, 21, 6, 19]
#c_list = [11, 30, 6, 15]

v_minus_c = [v-c for (v, c) in zip(v_list, c_list)]
total = sum([s for s in v_minus_c if s>0])
print(total)
