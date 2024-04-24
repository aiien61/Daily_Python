#! usr/bin/env python3
import re
import unittest
from toolz import pipe


def strip_by_regrex(*chars) -> str:
    if len(chars) == 1:
        strip_regrex = re.compile(r'\s*')
        return strip_regrex.sub('', chars[0])
    else:
        lstrip_regrex = re.compile(r'^' + chars[1] + r'*([.]{0,1})')
        rstrip_regrex = re.compile(r'([.]{0,1})' + chars[1] + r'*$')
        result = pipe(chars[0],
                      lambda string: lstrip_regrex.sub(r'\1', string),
                      lambda string: rstrip_regrex.sub(r'\1', string))
        return result
    
    
class Test(unittest.TestCase):
    strings = {
        '   xy-yx   ': None,
        '---xy-yx---': '-',
        'xy-yx------': '-',
        '------xy-yx': '-',
        'xy---yx': None, 
        '       ': None,
        'xy---yx': '-'
    }

    def test_regrex(self):
        for string, trailer in self.strings.items():
            if not trailer:
                expected = string.strip()
                actual = strip_by_regrex(string)
            else:
                expected = string.strip(trailer)
                actual = strip_by_regrex(string, trailer)
            self.assertEqual(actual, expected)
    

if __name__ == "__main__":
    unittest.main()
