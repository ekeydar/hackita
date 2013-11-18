import unittest
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

class PaliTests(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(is_palindrom("aba"))
        self.assertFalse(is_palindrom("abaa"))
        self.assertTrue(is_palindrom(""))
        self.assertTrue(is_palindrom("a"))
    
    def test_nonalpha(self):
        self.assertTrue(is_palindrom("ab a"))
        self.assertTrue(is_palindrom("ab,a"))
        
        

