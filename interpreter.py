from typing import List, TypeVar
from AST import AST, Node, insert, print_ast
from Tokens import *

A = TypeVar('A')
B = TypeVar('B')

# insert haskell


def get_token(token: str) -> Token:
    if token.isdigit():
        return Token(ty='INTEGER', value=token)
    elif token == '+':
        return ArithmeticToken(ty='ADD', value=None, ident=token)
    elif token == '-':
        return ArithmeticToken(ty='SUBTRACT', value=None, ident=token)
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


def execute_tokens(tokens: List[Token]) -> A:
    ast = AST()
    if any(map(lambda x: isinstance(x, AssignmentToken), tokens)):
        # partial_list = partition(tokens, [3])
        insert(ast.top, tokens)

        # print(tokens)
        print_ast(ast.top)
#        print(partial_list[0])
    else:
        print("has no assignmentToken")
