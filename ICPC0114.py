def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_prime(n):
    # Kiểm tra N có phải số nguyên tố hay không
    if not is_prime(n):
        return False
    
    # Kiểm tra từng chữ số và tổng các chữ số
    sum_digits = 0
    for digit in str(n):
        if digit not in '2357':  # Kiểm tra xem từng chữ số có phải là 2, 3, 5, 7 không
            return False
        sum_digits += int(digit)
    
    # Kiểm tra tổng các chữ số có phải số nguyên tố không
    if not is_prime(sum_digits):
        return False

    # Kiểm tra số đảo ngược có phải số nguyên tố không
    reversed_n = int(str(n)[::-1])
    if not is_prime(reversed_n):
        return False
    
    return True

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        if is_perfect_prime(N):
            print("Yes")
        else:
            print("No")
