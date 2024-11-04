import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def distance(self, another):
        return math.sqrt(math.pow(self.x-another.x, 2) + math.pow(self.y-another.y, 2))
    
if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        x1, y1, x2, y2, x3, y3 = map(int, input().split())
        a = Point(x1, y1)
        b = Point(x2, y2)
        c = Point(x3, y3)
        dis1 = Point.distance(a, b)
        dis2 = Point.distance(a, c)
        dis3 = Point.distance(c, b)
        if max(dis1, dis2, dis3) * 2 < dis1 + dis2 + dis3:
            # print("{:.3f}".format(dis1+dis2+dis3))
            my_list.append("{:.3f}".format(dis1+dis2+dis3))
        else:
            # print("INVALID")
            my_list.append('INVALID')
    for x in my_list:
        print(x)

