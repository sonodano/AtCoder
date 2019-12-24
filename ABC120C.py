s = str(input())

total = len(s)

zero = s.count('0')
one = s.count('1')

print(total - abs(zero-one))
