# time - O(n) space - O(n)
def evalRPN(tokens: list[str]) -> int:
    stack = []

    for t in tokens:
        if t not in "+-*/":
            stack.append(int(t))
        else:
            num2, num1 = stack.pop(), stack.pop()
            if t == '+':
                stack.append(num1 + num2)
            elif t == '-':
                stack.append(num1 - num2)
            elif t == '*':
                stack.append(num1 * num2)
            else:
                stack.append(int(num1 / num2))
    return stack[0]

def main():
    print(evalRPN(["2", "1", "+", "3", "*"]))
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


main()