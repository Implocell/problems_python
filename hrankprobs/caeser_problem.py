length = input()
string = input()
delta = int(input())

def cipher(string=string, delta=delta):
    result = ""

    for i in range(len(string)):
        char = string[i]

        if char.isupper():
            result += chr((ord(char) + delta-65) % 26 +65)
        elif char.islower():
            result += chr((ord(char) + delta - 97) % 26 +97)
        else:
            result += char
    
    return result

print(cipher())
