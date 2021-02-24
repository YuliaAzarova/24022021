A = [[(i+j+1)%2 for j in range(5)] for i in range(10)]
for i in range(5):
    for j in range(5):
        print(A[i][j], end = ' ')
    print()