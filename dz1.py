h, m, s = map(int, input().split())
#s, s2 = map(int, input())
k1 = h*3600
k1 += m*60
k1 += s
h2, m2, s2 = map(int, input().split())
k2 = h2*3600
k2 += m2*60
k2 += s2
print(k2 - k1)