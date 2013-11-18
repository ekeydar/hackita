def is_palindrom(word):
    if len(word) < 1:
        return True
    if not word[0].isalpha():
        return is_palindrom(word[1:])
    if not word[-1].isalpha():
        return is_palindrom(word[:-1])
    if word[0] == word[-1]:
        return is_palindrom(word[1:-1])
    return False

assert is_palindrom("aba")
assert not is_palindrom("abaa")
assert is_palindrom("")
assert is_palindrom("a")

assert is_palindrom(("ab a"))
assert is_palindrom(("ab,a"))


print __name__ + " OK!"
