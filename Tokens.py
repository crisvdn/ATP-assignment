class Token:
    def __init__(self, ty, value):
        self.type = ty
        self.value = value

    def __str__(self):
        return f"Token(type: {self.type}, value: {self.value})"

    def __repr__(self):
        return f"Token(type: {self.type}, value: {self.value})"


class OperatorToken(Token):
    pass


class ArithmeticToken(OperatorToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"ArithmeticToken(type: {self.type}, id: {self.ident})"


class VariableToken(Token):
    def __init__(self, ty, value, ident=None):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"VariableToken(type: {self.type}, value: {self.value}, id: {self.ident})"

    def __repr__(self):
        return f"VariableToken(type: {self.type}, value: {self.value}, id: {self.ident})"


class AssignmentToken(OperatorToken):
    def __init__(self, ty, value, ident=None):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"AssignmentToken(type: '{self.type}', operator: {self.ident} )"

    def __repr__(self):
        return f"AssignmentToken(type: '{self.type}', operator: {self.ident} )"


