import sys
l = list(input())

for x in l:
    if l.count(x) > 1:
        print('no')
        sys.exit(0)

print('yes')