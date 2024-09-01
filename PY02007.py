import sys

def solve():
    numbers = set()
    input_data = sys.stdin.read().split()
    for num in input_data:
        mod_value = int(num) % 42
        numbers.add(mod_value) 
    print(len(numbers))

if __name__ == "__main__":
    solve()
