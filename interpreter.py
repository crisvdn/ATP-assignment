from typing import List, TypeVar
from AST import AST, Node, insert, print_ast
from Tokens import *

A = TypeVar('A')
B = TypeVar('B')

# insert haskell
OPERATORS = {'+': lambda x, y: get_type(x) + get_type(y),
             '-': lambda x, y: get_type(x) - get_type(y),
             '*': lambda x, y: get_type(x) * get_type(y),
             '/': lambda x, y: int(get_type(x) / get_type(y))}


def get_token(token: str) -> Token:
    if token.isdigit():
        return IntegerToken(ty='INTEGER', value=token)
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


# tokenize :: str -> [Token]
def tokenize(tokens: str) -> List[Token]:
    if len(tokens) == 0:
        return []
    else:
        head, *tail = filter(str.strip, tokens)
        return [get_token(head)] + tokenize(tail)


# get_type :: A -> B
def get_type(value: A) -> B:
    if value.isdigit():
        return int(value)
    if value.isalpha():
        return str(value)


# is_first_precedence :: Token -> Bool
def is_first_precedence(value: Token) -> bool:
    return issubclass(type(value), FirstPrecedenceToken)


# is_second_precedence :: Token -> Bool
def is_second_precedence(value: Token) -> bool:
    return issubclass(type(value), SecondPrecedenceToken)


# partition :: [Token] -> int -> [[Token]]
def partition(alist: List[Token], indices: int) -> List[List[Token]]:
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]


# evaluate_expressions :: [Token] -> [Int] -> [Token]
def evaluate_expressions(expression: List[Token], precedence: List[int]) -> [Token]:
    # if one operator token left, evaluate that expression.
    if len(precedence) == 1 and len(expression) == 3:
        return [evaluate_expression(expression, 1)]
    # if multiply operators left, but one of that is first precedence(f.e multiply or divide).
    elif len(precedence) == 1 and issubclass(type(expression[precedence[0]]), FirstPrecedenceToken):
        return expression[:precedence[0] - 1] + [evaluate_expression(expression, precedence[0])] +\
               expression[precedence[0] + 2:]
    elif len(precedence) > 1 and issubclass(type(expression[precedence[0]]), FirstPrecedenceToken):

        return evaluate_expressions((expression[:precedence[0] - 1] + [evaluate_expression(expression, precedence[0])]
                                     + expression[precedence[0] + 2:]), list(map(lambda x: x - 2, precedence[1:])))
    else:
        return evaluate_expressions([evaluate_expression(expression, precedence[0])] + expression[3:],
                                    list(map(lambda x: x - 2, precedence[1:])))


# evaluate_expression :: [Token] -> Int -> Token
def evaluate_expression(expression: List[Token], operator_index: int) -> Token:
    return IntegerToken(ty='INTEGER',
                        value=str((OPERATORS[expression[operator_index].ident](expression[operator_index - 1].value,
                                                                               expression[operator_index + 1].value))))


# concat_int :: [Token] -> [Token]
def concat_int(tokens: List[Token]) -> List[Token]:
    if len(tokens) == 1:
        return [tokens[0]]
    else:
        if isinstance(tokens[0], IntegerToken) and isinstance(tokens[1], IntegerToken):
            tokens[0].value += tokens[1].value
            tokens.pop(1)
            return concat_int(tokens)
        elif isinstance(tokens[0], IntegerToken) and not isinstance(tokens[1], IntegerToken):
            return concat_int(tokens[1:]) + [IntegerToken(ty='INTEGER', value=tokens[0].value)]
        else:
            return concat_int(tokens[1:]) + [tokens[0]]


# execute :: List[Tokens] -> int
def execute(tokens: List[Token]) -> int:
    concatted_list = concat_int(tokens)
    concatted_list.reverse()
    print("\nconcatted list")
    print(concatted_list)

    # first evaluate precedence operators () * /
    # second evaluate operators + -
    first_precedence = list(i for i, x in enumerate(concatted_list) if is_first_precedence(x))
    if len(first_precedence) is not 0:
        concatted_list = evaluate_expressions(concatted_list, first_precedence)
    second_precedence = list(i for i, x in enumerate(concatted_list) if is_second_precedence(x))
    if len(second_precedence) is not 0:
        concatted_list = evaluate_expressions(concatted_list, second_precedence)
    return concatted_list
