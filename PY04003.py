import math 
class phanso:
    def __init__(self, tu, mau):
        self.tu = tu 
        self.mau = mau
    def rutgon(self):
        gcd = math.gcd(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd
        return f'{self.tu}/{self.mau}'

if __name__ == '__main__':
    a = input().split()
    x = phanso(int(a[0]), int(a[1]))
    print(x.rutgon())