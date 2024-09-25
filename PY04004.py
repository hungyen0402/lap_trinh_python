import math

class phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau 
    def rutgon(self):
        gcd = math.gcd(self.tu, self.mau)
        self.tu //= gcd
        self.mau //= gcd
    def cong_ps(self, other):
        gcd1 = math.gcd(self.mau, other.mau)
        lcd = (self.mau * other.mau) // gcd1
        self.tu = self.tu * (lcd // self.mau) + other.tu * (lcd // other.mau)
        self.mau = lcd
        self.rutgon()
        return f'{self.tu}/{self.mau}'
if __name__ == '__main__':
    a = input().split()
    x = phanso(int(a[0]), int(a[1]))
    y = phanso(int(a[2]), int(a[3]))
    print(x.cong_ps(y))