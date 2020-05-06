from typing import List, TypeVar
from AST import AST, recurs_ast
import AST

A = TypeVar('A')
B = TypeVar('B')


class Token:
    def __init__(self, ty, value):
        self.type = ty
        self.value = value

    def __str__(self):
        return f"Token(type: '{self.type}', value: '{self.value}'"

    def __repr__(self):
        return f"Token(type: '{self.type}', value: '{self.value}'"


class AritmeticToken(Token):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)


class VariableToken(Token):
    def __init__(self, ty, value, ident=None):
        self.ident = ident
        super().__init__(ty, value)


class AssignmentToken(Token):
    def __init__(self, ty, value, ident=None):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"AssignmentToken(type: '{self.type}', operator: '{self.ident}'"

    def __repr__(self):
        return f"AssignmentToken(type: '{self.type}', operator: '{self.ident}'"


# insert haskell


def get_token(token: str) -> Token:
    if token.isdigit():
        return Token(ty='INTEGER', value=token)
    elif token == '+':
        return AritmeticToken(ty='ADD', value=None, ident=token)
    elif token == '-':
        return AritmeticToken(ty='SUBTRACT', value=None, ident=token)
    elif token == '=':
        return AssignmentToken(ty='ASSIGN', value=None, ident=token)
    elif token.isalpha():
        return VariableToken(ty='VARIABLE', value=None, ident=token)


# insert haskell meuk hier


def tokenize(tokens: str) -> List[Token]:
    if len(tokens) == 0:
        return []
    else:
        head, *tail = filter(str.strip, tokens)
        return [get_token(head)] + tokenize(tail)


def get_type(value: A) -> B:
    if value.isdigit():
        return int(value)
    if value.isalpha():
        return str(value)


def partition(alist, indices):
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]


def execute(tokens: List[Token]) -> A:
    ast = AST.AST()
    if any(map(lambda x: isinstance(x, AssignmentToken), tokens)):
        a = partition(tokens, [1])
        print(a[1])
#        recurs_ast(ast, partition(tokens, 1))

    else:
        print("has no assignmentToken")
