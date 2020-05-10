from Tokens import VariableToken


class ProgramState:
    def __init__(self):
        self.vars = {}

    def __str__(self):
        return f"Variables: {self.vars}"

    __repr__ = __str__


# insert_variable :: ProgramState -> VariableToken -> ProgramState
def insert_variable(program_state: ProgramState, token: VariableToken) -> ProgramState:
    program_state.vars[token.ident] = token.value
    return program_state
