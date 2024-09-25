from decimal import Decimal 
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x = sqrt((self.x-other.x)**2 + (self.y-other.y)** 2)
        return x

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]), Decimal(arr[5]))
        if (p1.x == p2.x == p3.x or p1.y == p2.y == p3.y):
            print('INVALID')
        else:
            print("{:.3f}".format(p1.distance(p2)+p2.distance(p3)+p1.distance(p3)))