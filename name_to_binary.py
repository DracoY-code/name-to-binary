# name_to_binary.py

def to_binary(name):
    text = ''
    for let in name:
        code = ord(let)
        text += bin(code).replace('0b', '')
    return text


# __main__
string = input("Enter a name: ")
binary = to_binary(string)
print(binary)
