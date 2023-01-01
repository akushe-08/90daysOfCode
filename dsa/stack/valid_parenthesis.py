def is_valid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    dic = {")": "(", "]": "[", "}": "{"}

    stk = []

    for char in s:
        if char not in dic:
            stk.append(char)
        else:
            if dic[char] == stk[-1]:
                stk.pop()
    return not stk


print(is_valid("[[]]"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
