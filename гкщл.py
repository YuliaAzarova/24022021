def isPal(s):  # на вход подадим строку
    # s[::-1] - перевернутая строка
    return s == s[::-1]


def f(n):  # факториал числа 6 это 6! = 1*2*3*4*5*6
    ans = 1
    for i in range(n):  # 0,1,...,n-1
        ans *= i + 1
    return ans


x = int(input())
print(f(x))