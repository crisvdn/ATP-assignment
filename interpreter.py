from typing import List, TypeVar, Any
from Tokens import *
from program_state import *

A = TypeVar('A')
B = TypeVar('B')

# insert haskell
OPERATORS = {'[': lambda x, y: get_type(x) + get_type(y),
             '-': lambda x, y: get_type(x) - get_type(y),
             '_': lambda x, y: get_type(x) * get_type(y),
             '$': lambda x, y: int(get_type(x) / get_type(y))}

# get_token :: str -> Token
def get_token(token: str, line: int, position: int) -> Token:
    if token.isdigit():
        return IntegerToken(ty='INTEGER', value=token, line=line, pos=position)
    elif token == '[':
        return AdditionToken(ty='ADD', value=None, ident=token, line=line, pos=position)
    elif token == '-':
        return SubtractToken(ty='SUBTRACT', value=None, ident=token, line=line, pos=position)
    elif token == ':':
        return AssignmentToken(ty='ASSIGN', value=None, ident=token, line=line, pos=position)
    elif token.isalpha():
        return VariableToken(ty='VARIABLE', value=None, ident=token, line=line, pos=position)
    elif token == '_':
        return MultiplyToken(ty='MULTIPLY', value=None, ident=token, line=line, pos=position)
    elif token == '$':
        return DivideToken(ty='DIVIDE', value=None, ident=token, line=line, pos=position)
    elif token == '(':
        return LParenToken(ty='LParenthesis', value=None, ident=token, line=line, pos=position)
    elif token == ')':
        return RParenToken(ty='RParenthesis', value=None, ident=token, line=line, pos=position)


# tokenize :: (str -> int -> int) -> [Token]
def tokenize(tokens: str, line: int, position: int) -> List[Token]:
    if len(tokens) == 0:
        return []
    else:
        head, *tail = filter(str.strip, tokens)
        return [get_token(head, line, position)] + tokenize(tail, line + 1, position + 1)


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


# get_precedence_token :: [Token] -> A -> [Token]
def get_type_token(tokens: List[Token], type_any: Any) -> List[Token]:
    return list(filter(lambda x: isinstance(x, type_any), tokens))


# get_prec_tokens :: [Token] -> [Token]
def get_prec_tokens(tokens: List[Token]) -> List[Token]:
    return list(filter(lambda x: (issubclass(type(x), PrecedenceToken) or issubclass(type(x), IntegerToken)), tokens))


# partition :: [Token] -> int -> [[Token]]
def partition(alist: List[Token], indices: int) -> List[List[Token]]:
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]


# evaluate_expressions :: [Token] -> [Int] -> [Token]
def evaluate_expressions(expression: List[Token], precedence: List[int]) -> [Token]:
    # if one operator token left, evaluate that expression.
    if len(precedence) == 1 and len(expression) == 3:
        return [evaluate_expression(expression, 1)]
    # if one first_precedence operator remains and one or more of second_precedence operators(f.e addition or subtract).
    elif len(precedence) == 1 and issubclass(type(expression[precedence[0]]), FirstPrecedenceToken):
        return expression[:precedence[0] - 1] + [evaluate_expression(expression, precedence[0])] +\
               expression[precedence[0] + 2:]
    # if multiple precedence tokens are left of first precedence type.
    elif len(precedence) > 1 and issubclass(type(expression[precedence[0]]), FirstPrecedenceToken):
        return evaluate_expressions((expression[:precedence[0] - 1] + [evaluate_expression(expression, precedence[0])]
                                     + expression[precedence[0] + 2:]), list(map(lambda x: x - 2, precedence[1:])))
    # if multiple second precedence tokens are left.
    else:
        return evaluate_expressions([evaluate_expression(expression, precedence[0])] + expression[3:],
                                    list(map(lambda x: x - 2, precedence[1:])))


# evaluate_expression :: [Token] -> Int -> Token
def evaluate_expression(expression: List[Token], operator_index: int) -> Token:
    # This will return an IntegerToken from 3 tokens. F.e. (5 + 5) returns an integerToken with value 10.
    # Operator lambda function from OPERATORS will be used.
    return IntegerToken(ty='INTEGER',
                        value=str((OPERATORS[expression[operator_index].ident](expression[operator_index - 1].value,
                                                                               expression[operator_index + 1].value))))


# assign_value_to_variable :: [Token] -> Token
def assign_value_to_variable(expression: List[Token]) -> Token:
    # This rerturns a VariableToken and assigns the value to that variable.
    if expression[2].value is not None:
        return VariableToken(ty=expression[0].type, value=expression[2].value, ident=expression[0].ident)
    else:
        print("no value")


# concat_int :: [Token] -> [Token]
def concat_int(tokens: List[Token]) -> List[Token]:
    # This concatanates multiple IntegerTokens after each other.
    # F.e. 55 + 5 will be initially build as [IntegerToken(5), IntegerToken(5), AdditionToken(+), IntegerToken(5)
    # This function returns (IntegerToken(55), AdditionToken(+), IntegerToken(5)
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


# execute :: ProgramState -> List[Tokens] -> ProgramState
def execute(program_state: ProgramState, tokens: List[Token]) -> ProgramState:
    concatted_list = concat_int(tokens)
    concatted_list.reverse()

    # assignment and variables will be extracted into assign_var_tokens
    assign_var_tokens = get_type_token(concatted_list, VariableToken) + get_type_token(concatted_list, AssignmentToken)

    # precedence tokens(integers, operators) will be extracted into precedence_tokens
    precedence_tokens = get_prec_tokens(concatted_list)

    # First precedence tokens are extracted
    first_precedence = list(i for i, x in enumerate(precedence_tokens) if is_first_precedence(x))

    # if there are first precedence tokens, evaluate that expression
    if len(first_precedence) is not 0:
        precedence_tokens = evaluate_expressions(precedence_tokens, first_precedence)
    # Second precedence tokens are extracted
    second_precedence = list(i for i, x in enumerate(precedence_tokens) if is_second_precedence(x))
    # if there are second precedence tokens, evaluate that expression
    if len(second_precedence) is not 0:
        precedence_tokens = evaluate_expressions(precedence_tokens, second_precedence)
    # If a variable needs to be assigned, return it into the program state.
    if assign_var_tokens:
        return insert_variable(program_state, assign_value_to_variable(assign_var_tokens  + precedence_tokens))
    # else return evaluation
    else:
        return precedence_tokens
