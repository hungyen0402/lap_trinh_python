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