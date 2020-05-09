from typing import List, TypeVar
from functools import reduce
from AST import AST, Node, insert, print_ast
from Tokens import *

A = TypeVar('A')
B = TypeVar('B')

# insert haskell
OPERATORS = {'+': lambda x, y: get_type(x) + get_type(y),
             '-': lambda x, y: get_type(x) - get_type(y),
             '*': lambda x, y: get_type(x) * get_type(y),
             '/': lambda x, y: get_type(x) / get_type(y)}


def get_token(token: str) -> Token:
    if token.isdigit():
        return Token(ty='INTEGER', value=token)
    elif token == '+':
        return AdditionToken(ty='ADD', value=None, ident=token)
    elif token == '-':
        return SubtractToken(ty='SUBTRACT', value=None, ident=token)
    elif token == '=':
        return AssignmentToken(ty='ASSIGN', value=None, ident=token)
    elif token.isalpha():
        return VariableToken(ty='VARIABLE', value=None, ident=token)
    elif token == '*':
        return MultiplyToken(ty='MULTIPLY', value=None, ident=token)
    elif token == '/':
        return DivideToken(ty='DIVIDE', value=None, ident=token)
    elif token == '(':
        return LParenToken(ty='LParenthesis', value=None, ident=token)
    elif token == ')':
        return RParenToken(ty='RParenthesis', value=None, ident=token)


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


def is_first_precedence(value) -> bool:
    return issubclass(type(value), FirstPrecedenceToken)


def is_second_precedence(value) -> bool:
    return issubclass(type(value), SecondPrecedenceToken)


def partition(alist, indices):
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]


def evaluate_expression(expression: List[Token], operatorIndex: int) -> int:
    # if expression[operatorIndex]
    return OPERATORS[expression[operatorIndex].ident](expression[operatorIndex - 1].value, expression[operatorIndex + 1].value)


def execute(tokens: List[Token])-> int:
    # first evaluate precedence operators () * /
    # second evaluate operators + -
    first_precedence = list(i for i, x in enumerate(tokens) if is_first_precedence(x))
    second_precedence = list(i for i, x in enumerate(tokens) if is_second_precedence(x))

    # for i, j in enumerate(tokens):
    #     print(type(j))
    #     if issubclass(type(j), ArithmeticToken):
    #         print("HIT:", i, j)
    #     else:
    #         print(type(i))
    if len(first_precedence) is not 0:
        print(evaluate_expression(tokens, first_precedence[0]))
    if len(second_precedence) is not 0:
        print(evaluate_expression(tokens, second_precedence[0]))


def execute_tokens(tokens: List[Token]) -> A:
    ast = AST()
    execute(tokens)
#
#     if any(map(lambda x: isinstance(x, AssignmentToken), tokens)):
#         # partial_list = partition(tokens, [3])
#         insert(ast.top, tokens)
#
#         # print(tokens)
#         print_ast(ast.top)
# #        print(partial_list[0])
#     else:
#         print("has no assignmentToken")
#