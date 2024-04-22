#! /usr/bin/env python3
import re
from termcolor import colored


def show_match(regrex: object, text: str) -> None:
    try:
        print(regrex.findall(text))
    except AttributeError as e:
        print(colored('No matched string found', on_color='on_red'))

