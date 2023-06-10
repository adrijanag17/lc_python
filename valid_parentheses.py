# time - O(n) space - O(n)
def valid_parentheses(s: str) -> bool:
    stack = []

    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif not stack or c != stack.pop():
            return False
    return not stack


# time - O(n) space - O(n)
def valid_parentheses2(s: str) -> bool:
    stack = []

    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if not stack or ((c == ')' and stack[-1] != '(') or 
            (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '[')):
                return False
            stack.pop()

    return not stack


def main():
    print(valid_parentheses("({[]})"))
    print(valid_parentheses("({)}"))
    print(valid_parentheses("()]["))


main()