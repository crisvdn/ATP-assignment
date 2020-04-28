from typing import List, TypeVar
import re

my_tokens = []

class Token:
    def __init__(self, ty, value):
        self.type = ty
        self.value = value

    def __str__(self):
        return f"Token(type='{self.type}',value={self.value}')"

    __repr__ = __str__

# insert haskell


def get_token(token: str) -> Token:
    if token.isdigit():
        return Token(ty='INTEGER', value=token)
    elif token == '+':
        return Token(ty='ADD', value='+')
    elif token == '-':
        return Token(ty='SUBTRACT', value='-')


# insert haskell meuk hier


def tokenize(tokens: str) -> List[Token]:
    if len(tokens) == 0:
        return []
    else:
        head, *tail = filter(str.strip, tokens)
        return [get_token(head)] + tokenize(tail)
