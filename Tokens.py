class Token:
    def __init__(self, ty, value):
        self.type = ty
        self.value = value

    def __str__(self):
        return f"Token(type: {self.type}, value: {self.value})"

    def __repr__(self):
        return f"Token(type: {self.type}, value: {self.value})"


class IntegerToken(Token):
    def __init__(self, ty, value):
        super().__init__(ty, value)

    def __str__(self):
        return f"IntegerToken(type: {self.type}, value: {self.value})"

    def __repr__(self):
        return f"IntegerToken(type: {self.type}, value: {self.value})"


class OperatorToken(Token):
    pass


class PrecedenceToken(OperatorToken):
    pass


class FirstPrecedenceToken(PrecedenceToken):
    pass


class SecondPrecedenceToken(PrecedenceToken):
    pass


class MultiplyToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"MultiplyToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"MultiplyToken(type: {self.type}, id: {self.ident})"


class DivideToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"DivideToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"DivideToken(type: {self.type}, id: {self.ident})"


class LParenToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"LParenToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"LParenToken(type: {self.type}, id: {self.ident})"


class RParenToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"RParenToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"RParenToken(type: {self.type}, id: {self.ident})"


class AdditionToken(SecondPrecedenceToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"AdditionToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"AdditionToken(type: {self.type}, id: {self.ident})"


class SubtractToken(SecondPrecedenceToken):
    def __init__(self, ty, value, ident):
        self.ident = ident
        super().__init__(ty, value)

    def __str__(self):
        return f"SubtractToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"SubtractToken(type: {self.type}, id: {self.ident})"


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
