def reverse(s: str) -> str:
    result = ""
    for letter in s:
        result = letter + result
    return result

def reverse_pythonic(s: str) -> str:
    return s[::-1]

def reverse_loops(s: str, while_loop: bool = False) -> str:
    result = []
    index = len(s)
    if not while_loop:
        for i in range(1, index +1):
            result.append(s[-i])
    
    else:
        while index > 0:
            result += s[index - 1]
            index -= 1
    
    return "".join(result)


def is_palindrome(s: str) -> bool:
    reversed_s = reverse(s)
    if s.lower() == reversed_s.lower():
        return True
    else:
        return False

text_to_test = input("Please input text to test if it palindrome: ")
print(is_palindrome(text_to_test))
