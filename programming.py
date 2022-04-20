'''
1. You are given a 2D matrix of dimensions m * n consisting of
integers, and an integer k. Your task is to print “true” if the
element k lies in the matrix and “false” otherwise. If the element
exists then print the index in a new line.
Each row and column is in sorted order, and the first element of a
row is greater than the last element of the previous row.
'''

def matrix(m, n, k):
    a = [[0]*n]*m
    c = 0
    for i in range(m):
        b = []
        for j in range(n):
            b.append(int(input()))
            if b[-1] == k:
                c = 1
                x = i; y = j
        a[i] = b
    if c == 1:
        print("True")
        print(x, y)


m = int(input("m"))
n = int(input("n"))
k = int(input("k"))
matrix(m, n, k)

