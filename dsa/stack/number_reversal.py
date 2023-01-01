def reverse(num):
    if num == 0:
        return 0

    stk = []

    while num:
        stk.append(num % 10)
        num //= 10

    # num will be zero at this point

    tens = 1
    while stk:
        num = stk[-1] * tens + num
        tens *= 10
        stk.pop()

    return num


print(reverse(12305))
