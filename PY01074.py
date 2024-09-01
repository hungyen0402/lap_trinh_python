import math

f = [0] * (2*(10**6)+1)
for i in range(0, 2000001, 1):
    id = True
    for j in range(2, int(math.sqrt(i))+1, 1):
        if i % j == 0:
            f[i] = f[j] + f[i//j]
            id = False
            break
    if id: 
        f[i] = i
if __name__ == '__main__':
    sum = 0
    for _ in range(int(input())):
        x = int(input())
        sum += f[x]
    print(sum)

