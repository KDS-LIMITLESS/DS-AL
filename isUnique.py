# Q.S Implement an algorithm to determine if a string has all unique characters.

def isUnique(string: str):
    v: list = []
    for character in string:
        if character in v:
            return False
        v.append(character)
    print(v)
    return True


print(isUnique('abcdefghijklmnopqrstuvwxyz'))