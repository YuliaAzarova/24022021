year = int(input())
if year % 4 == 0 or year % 400 == 0:
    print('YES')
elif year % 100 == 1:
    print('NO')
else:
    print('NO')