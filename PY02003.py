a =set()
max = int(1e18)
for i in range(65): #2^40 > max
    n2 = 1<<i
    if n2 > max: break
    for j in range(40):
        n3 = 3 ** j
        if n2*n3 > max: break
        for k in range(28):
            n5 = 5 ** k
            if n2*n3*n5 > max: break 
            a.add(n2*n3*n5)
a = sorted(a)

def find_ans(l, r, v):
    if l > r: return 'Not in sequence'
    mid = (l+r)>>1
    if a[mid] == v: return mid + 1
    if a[mid] < v: return find_ans(mid+1, r, v)
    return find_ans(l, mid-1, v) 
        
if __name__ == '__main__':
    for _ in range(int(input())):
        print(find_ans(0, len(a), int(input())))
