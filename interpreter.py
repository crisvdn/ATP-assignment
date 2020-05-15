from typing import List, TypeVar, Any
from Tokens import *
from program_state import *

A = TypeVar('A')
B = TypeVar('B')

# insert haskell
OPERATORS = {'[': lambda x, y: get_type(x) + get_type(y),
             '-': lambda x, y: get_type(x) - get_type(y),
             '_': lambda x, y: get_type(x) * get_type(y),
             '$': lambda x, y: int(get_type(x) / get_type(y)),
             '{': lambda x, y: bool(get_type(x) < get_type(y)),
             '}': lambda x, y: bool(get_type(x) > get_type(y)),
             }

OPS = {':', '-', '}', '{', '$', '_', '['}

keywords = []


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
    elif token in keywords:
        pass
        # to do
    elif token == '_':
        return MultiplyToken(ty='MULTIPLY', value=None, ident=token, line=line, pos=position)
    elif token == '$':
        return DivideToken(ty='DIVIDE', value=None, ident=token, line=line, pos=position)
    elif token == '(':
        return LParenToken(ty='LParenthesis', value=None, ident=token, line=line, pos=position)
    elif token == ')':
        return RParenToken(ty='RParenthesis', value=None, ident=token, line=line, pos=position)
    elif token == '{':
        return RelationalToken(ty='LessThan', value=None, ident=token, line=line, pos=position)
    elif token == '}':
        return RelationalToken(ty='GreaterThan', value=None, ident=token, line=line, pos=position)
    elif len(token) >= 1 and token[0].isalpha():
        return VariableToken(ty='VARIABLE', value=None, ident=token, line=line, pos=position)
    elif token == '!':
        return ConditionStatementToken(ty='CONDITION', value=None, ident=token, line=line, pos=position)
    elif token == '?':
        return ConditionalExpressionToken(ty='CONDITION', value=None, ident=token, line=line, pos=position)
    else:
        print(token, "not a valid token")


# tokenize :: (str -> int -> int) -> [Token]
def tokenize(tokens: List[str], line: int, position: int) -> List[Token]:
    if len(tokens) == 0:
        return []
    else:
        head, *tail = tokens
        return [get_token(head, line, position)] + tokenize(tail, line, position + 1)


# get_type :: A -> B
def get_type(value: A) -> B:
    if value is not None and isinstance(value, str):
        if value.isdigit():
            return int(value)
        if value.isalpha():
            return str(value)
    elif isinstance(value, int):
        return value
    elif value is None:
        return 0


# is_first_precedence :: (Token -> Any) -> Bool
def is_type_precedence(value: Token, type_any: Any) -> bool:
    return issubclass(type(value), type_any)


# get_precedence_token :: ([Token] -> A) -> [Token]
def get_type_token(tokens: List[Token], type_any: Any) -> List[Token]:
    if type_any == ConditionalToken:
        return tokens[1:]
    if type_any == VariableToken:
        return tokens[:2]
    else:
        return list(filter(lambda x: isinstance(x, type_any), tokens))


# get_prec_tokens :: [Token] -> [Token]
def get_prec_tokens(tokens: List[Token]) -> List[Token]:
    if isinstance(tokens[0], VariableToken) and isinstance(tokens[1], AssignmentToken):
        return tokens[2:]
    else:
        return list(filter(lambda x: (issubclass(type(x), PrecedenceToken) or issubclass(type(x), IntegerToken)), tokens))


# partition :: ([Token] -> int) -> [[Token]]
def partition(alist: List[Token], indices: int) -> List[List[Token]]:
    return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]


# evaluate_expressions :: (ProgramState -> [Token] -> [Int]) -> [Token]
def evaluate_expressions(ps: ProgramState, expression: List[Token], precedence: List[int]) -> [Token]:
    # if one operator token left, evaluate that expression.
    if len(precedence) == 1 and len(expression) == 3:
        return [evaluate_expression(ps, expression, 1)]
    # if one first_precedence operator remains and one or more of second_precedence operators(f.e addition or subtract).
    elif len(precedence) == 1 and issubclass(type(expression[precedence[0]]), FirstPrecedenceToken)\
            or issubclass(type(expression[precedence[0]]), SecondPrecedenceToken):
        return expression[:precedence[0] - 1] + [evaluate_expression(ps, expression, precedence[0])] +\
               expression[precedence[0] + 2:]
    # if multiple precedence tokens are left of first precedence type.
    elif len(precedence) > 1 and issubclass(type(expression[precedence[0]]), FirstPrecedenceToken):
        return evaluate_expressions(ps,
                                    (expression[:precedence[0] - 1] +
                                     [evaluate_expression(ps, expression, precedence[0])]
                                     + expression[precedence[0] + 2:]), list(map(lambda x: x - 2, precedence[1:])))
    # if multiple second precedence tokens are left.
    else:
        return evaluate_expressions(ps, [evaluate_expression(ps, expression, precedence[0])] + expression[3:],
                                    list(map(lambda x: x - 2, precedence[1:])))


# evaluate_expression :: (ProgramState -> [Token] -> Int) -> Token
def evaluate_expression(ps: ProgramState, expression: List[Token], operator_index: int) -> Token:
    # This will return an IntegerToken from 3 tokens. F.e. (5 + 5) returns an integerToken with value 10.
    # Operator lambda function from OPERATORS will be used.
    if isinstance(expression[0], IntegerToken):
        return IntegerToken(ty='INTEGER', line=expression[operator_index -1].line,
                            pos=expression[operator_index -1].pos,
                            value=(OPERATORS[expression[operator_index].ident]
                                       (expression[operator_index - 1].value,
                                        expression[operator_index + 1].value)))
    elif isinstance(expression[0], VariableToken) and isinstance(expression[2], IntegerToken):
        # if variable token is inside programstate variables
        if expression[0].ident in ps.vars:
            return VariableToken(ty='VARIABLE',
                                 ident=expression[0].ident,
                                 value=str(OPERATORS[expression[operator_index].ident](ps.vars[expression[0].ident],
                                expression[operator_index + 1].value)), line=expression[operator_index - 1].line,
                                 pos=expression[operator_index - 1].pos)
        else:
            # variable doesnt exist. throw error
            print('error, var doesnt exist')
    elif isinstance(expression[0], VariableToken) and isinstance(expression[2], VariableToken):
        if expression[0].ident in ps.vars and expression[2].ident in ps.vars:
            return VariableToken(ty='VARIABLE',
                                 ident=expression[0].ident,
                                 value=OPERATORS[expression[operator_index].ident](ps.vars[expression[0].ident],
                                            ps.vars[expression[2].ident]), line=expression[operator_index - 1].line,
                                 pos=expression[operator_index - 1].pos)
        else:
            # one of the variables doesnt exist.
            if expression[0].ident not in ps.vars:
                print(f"error: {expression[0]} is not assigned.")
            else:
                print(f"error: {expression[2]} is not assigned.")
    else:
        print("err")


# execute_loop :: (ProgramState -> [Token] -> [Token]) -> ProgramState:
def execute_loop(ps: ProgramState, conditional_statement: List[Token], conditional_expression: List[Token]) -> ProgramState:
    # conditional statement list enters
    if evaluate_expression(ps, conditional_statement, 1).value:
        # assignment and variables will be extracted into assign_var_tokens
        assign_var_tokens = get_type_token(conditional_expression, VariableToken)
        # precedence tokens(integers, operators) will be extracted into precedence_tokens
        precedence_tokens = get_prec_tokens(conditional_expression)

        first_precedence = list(i for i, x in enumerate(conditional_expression)
                                if is_type_precedence(x, FirstPrecedenceToken))

        # if there are first precedence tokens, evaluate that expression
        if len(first_precedence) is not 0:
            precedence_tokens = evaluate_expressions(ps, precedence_tokens, first_precedence)
        # Second precedence tokens are extracted
        second_precedence = list(i for i, x in enumerate(precedence_tokens)
                                 if is_type_precedence(x, SecondPrecedenceToken))
        # if there are second precedence tokens, evaluate that expression
        if len(second_precedence) is not 0:
            precedence_tokens = evaluate_expressions(ps, precedence_tokens, second_precedence)
        # If a variable needs to be assigned, return it into the program state.

        # if there are third precedence tokens, evaluate that expression
        third_precedence = list(i for i, x in enumerate(precedence_tokens)
                                if is_type_precedence(x, ThirdPrecedenceToken))

        if len(third_precedence) is not 0:
            precedence_tokens = evaluate_expressions(ps, precedence_tokens, third_precedence)
        if assign_var_tokens:
            return insert_variable(ps, assign_value_to_variable(assign_var_tokens + precedence_tokens))
        # else return evaluation
        else:
            return precedence_tokens
    else:
        print("err")
        return ps


# assign_value_to_variable :: [Token] -> Token
def assign_value_to_variable(expression: List[Token]) -> VariableToken:
    # This returns a VariableToken and assigns the value to that variable.
    if expression[2].value is not None:
        return VariableToken(ty=expression[0].type, value=expression[2].value, ident=expression[0].ident)
    else:
        print("no value")


# execute :: ProgramState -> List[Tokens] -> ProgramState
def execute(program_state: ProgramState, tokens: List[Token]) -> ProgramState:
    concatted_list = tokens

    # assignment and variables will be extracted into assign_var_tokens
    assign_var_tokens = get_type_token(concatted_list, VariableToken)
    # precedence tokens(integers, operators) will be extracted into precedence_tokens
    precedence_tokens = get_prec_tokens(concatted_list)
    # Filter out loop condition

    loop_con = concatted_list.index(next(filter(lambda x: isinstance(x, ConditionStatementToken),
                                         concatted_list), concatted_list[-1]))

    if isinstance(concatted_list[loop_con], ConditionStatementToken):
        loop_exp = concatted_list.index(next(filter(lambda x: isinstance(x, ConditionalExpressionToken),
                                         concatted_list), concatted_list[0]))
        loop_con_expr = partition(concatted_list, [loop_exp])
        return execute_loop(program_state, loop_con_expr[loop_con][1:], loop_con_expr[1][1:])

    else:
        # First precedence tokens are extracted
        first_precedence = list(i for i, x in enumerate(precedence_tokens) if is_type_precedence(x, FirstPrecedenceToken))

        # if there are first precedence tokens, evaluate that expression
        if len(first_precedence) is not 0:
            precedence_tokens = evaluate_expressions(program_state, precedence_tokens, first_precedence)
        # Second precedence tokens are extracted
        second_precedence = list(i for i, x in enumerate(precedence_tokens) if is_type_precedence(x, SecondPrecedenceToken))
        # if there are second precedence tokens, evaluate that expression
        if len(second_precedence) is not 0:
            precedence_tokens = evaluate_expressions(program_state, precedence_tokens, second_precedence)
        # If a variable needs to be assigned, return it into the program state.

        # if there are third precedence tokens, evaluate that expression
        third_precedence = list(i for i, x in enumerate(precedence_tokens) if is_type_precedence(x, ThirdPrecedenceToken))

        if len(third_precedence) is not 0:
            precedence_tokens = evaluate_expressions(program_state, precedence_tokens, third_precedence)
        if assign_var_tokens:
            return insert_variable(program_state, assign_value_to_variable(assign_var_tokens + precedence_tokens))
        # else return evaluation
        else:
            return precedence_tokens
