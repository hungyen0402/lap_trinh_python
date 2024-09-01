def snt(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
import sys
from array import array
# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     matrix = []
#     for _ in range(n):
#         row = list(map(int, input().split()))
#         for j in range(m):
#             row[j] = 1 if snt(row[j]) else 0
#         matrix.append(row)
#     for row in matrix:
#         print(' '.join(map(str, row)))

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    n , m = int(data[0], data[1])
    id = 2
    matrix = []
    for _ in range(n):
        row = array('i')
        for j in range(m):
            value = int(data[id])
            row.append(1 if snt(value) else 0)
            id += 1
        matrix.append(row)
    for row in matrix:
        print(' '.join(map(str, row)))
    
