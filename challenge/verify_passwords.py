#! usr/bin/env python3
import re
import unittest

def verify_password(password: str) -> bool:
    lowercase_regrex = re.compile(r'[a-z]+')
    if lowercase_regrex.search(password) is None:
        return False
    
    uppercase_regrex = re.compile(r'[A-Z]+')
    if uppercase_regrex.search(password) is None:
        return False
    
    digit_regrex = re.compile(r'\d+')
    if digit_regrex.search(password) is None:
        return False
    
    length_regrex = re.compile(r'(.{8})(.*)')
    if length_regrex.search(password) is None:
        return False
    
    return True

class Test(unittest.TestCase):
    passwords = {
        'a8cDefgh': True,
        'a8cDefghx': True,
        'a8cD-efgh*_%$@129451': True,
        'a8cdefgh': False,
        'abcDefgh': False,
        'A8CDEFGH': False,
        'a8c': False
    }

    def test_verify_password(self):
        for password, expected in self.passwords.items():
            actual = verify_password(password)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
