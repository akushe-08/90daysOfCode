total = 0


def n_to_one(n: int):
    """Prints numbers from n to 1 using recursion"""
    if n == 0:
        return
    print(n)
    n_to_one(n - 1)


def one_to_n(n: int):
    """Prints numbers from 1 to n using recursion"""

    if n == 0:
        return
    one_to_n(n - 1)
    print(n)


def factorial(n: int):
    """
    Returns factorial of a number
    Inefficient as doesn't use memoization
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_of_n_nums(n: int):
    """Returns sum of consecutive nums from n to 0"""
    if n == 0:
        return 0
    return n + sum_of_n_nums(n - 1)


def sum_of_digits(n: int):
    if n == 0:
        return 0
    return sum_of_digits(n // 10) + n % 10


def product_of_digits(n: int):
    if n % 10 == n:
        return n

    return product_of_digits(n // 10) * (n % 10)


def reverse_a_num(n: int):
    global total
    if n % 10 == n:
        return n
    total = total * 10 + (n % 10)
    total += reverse_a_num(n // 10)
    # total += (n % 10)*10 + reverse_a_num(n // 10)

if __name__ == "__main__":
    # n_to_one(10)
    # one_to_n(10)
    # print(factorial(5))
    # print(sum_of_n_nums(5))
    print(reverse_a_num(481))
    print(total)
