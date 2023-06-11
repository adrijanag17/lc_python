# time - O(n) space - O(1) where n = len(s)
def is_alnum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


def valid_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not is_alnum(s[l]):
            l += 1
        while r > l and not is_alnum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


# time - O(n) space - O(n) where n is the length of the string
def valid_palindrome2(s: str) -> bool:
    new_str = "".join(c.lower() for c in s if c.isalnum())

    l, r = 0, len(new_str) - 1
    while l < r:
        if new_str[l] != new_str[r]:
            return False
        l, r = l + 1, r - 1
    return True


# time - O(n) space - O(n) where n = len(s)
def valid_pal(s: str) -> bool:
    newS = "".join(c.lower() for c in s if c.isalnum())
    newR = newS[::-1]
    return newS == newS[::-1]



def main():
    print(valid_palindrome("A man, a plan, a canal: Panama"))
    print(valid_palindrome("race a car"))
    print(valid_palindrome(" "))


main()