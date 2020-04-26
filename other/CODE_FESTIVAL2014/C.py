#%%
a, b = map(int, input().split())

#%%
# 始点のうるう年
if a % 4 == 0:
    a = a
elif (a + 1) % 4 == 0:
    a = a + 1
elif (a + 2) % 4 == 0:
    a = a + 2
elif (a + 3) % 4 == 0:
    a = a + 3
# 終点のうるう年
if b % 4 == 0:
    b = b
elif (b - 1) % 4 == 0:
    b = b - 1
elif (b - 2) % 4 == 0:
    b = b - 2
elif (b - 3) % 4 == 0:
    b = b - 3

#%%
leap = (b - a) // 4 + 1

#100の倍数について
if a % 100 != 0:
    st100 = (a//100 + 1) * 100
else:
    st100 = a
if b % 100 != 0:
    end100 = b//100 * 100
else:
    end100 = b

if st100 >  end100:
    m100 = 0
elif st100 < end100:
    m100 = (end100 - st100) // 100 + 1
else:
    m100 = 1

# 400の倍数について
if a % 400 != 0:
    st400 = (a//400 + 1) * 400
else:
    st400 = a
if b % 400 != 0:
    end400 = b//400 * 400
else:
    end400 = b

if st400 >  end400:
    m400 = 0
elif st400 < end400:
    m400 = (end400 - st400) // 400 + 1
else:
    m400 = 1

ans = leap - m100 + m400
print(ans)