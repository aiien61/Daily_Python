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
        rstrip_regrex = re.compile(r'([.]{0,1}' + chars[1] + r'*$)')
        result = pipe(chars[0],
                      lambda string: lstrip_regrex.sub('\1', string),
                      lambda string: rstrip_regrex.sub('\1', string))
        return result
    
class Test(unittest.TestCase):
    strings = ['---xy-yx---']
    

if __name__ == "__main__":
    print('---xy-yx---'.strip('-'))
    # print(re.compile(r'^-*([.]{0,1})').sub('\1', '---xy-x--'))
    # print(re.compile(r'([.]{0,1})-*$').sub('\1', '---xy-yx--'))
    print(strip_by_regrex('         '))