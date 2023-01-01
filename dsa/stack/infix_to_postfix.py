from stack_using_linked_list import Stack

precedence = {"^": 5, "*": 4, "/": 3, "+": 2, "-": 1}

ex = {"1+3*5-8/2": "135*+82/-"}


def to_postfix(infix: str):
    out = ""
    stk = Stack()
    for char in infix:
        if char.isdigit() or char.isalpha():
            out += char
        else:
            if not stk or (char == "("):
                stk.push(char)
            else:
                if char == ")":
                    while stk.top() != "(":
                        out += stk.pop()
                    stk.pop()
                elif stk.top() == "(":
                    stk.push(char)
                elif precedence[char] > precedence[stk.top()]:
                    stk.push(char)
                else:
                    while not stk.is_empty():
                        if stk.top() == "(":
                            break
                        out += stk.pop()
                    stk.push(char)
    while not stk.is_empty():
        out += stk.pop()
    return out


ret = to_postfix("1+3*5-8/2")
ret = to_postfix("1+3-5-6*2")
ret = to_postfix("2+3-((5+2)*3)")
ret = to_postfix("A*(B+C)/D")
ret = to_postfix("a+b*(c^d-e)^(f+g*h)-i")
print(ret)
