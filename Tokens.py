class Token:
    def __init__(self, ty, value, line=0, pos=0):
        self.type = ty
        self.value = value
        self.line = line
        self.pos = pos

    def __str__(self):
        return f"Token(type: {self.type}, value: {self.value})"

    def __repr__(self):
        return f"Token(type: {self.type}, value: {self.value}, line: {self.line}, pos: {self.pos})"


class IntegerToken(Token):
    def __init__(self, ty, value, line, pos):
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"IntegerToken(type: {self.type}, value: {self.value})"

    def __repr__(self):
        return f"IntegerToken(type: {self.type}, value: {self.value}, line: {self.line}, pos: {self.pos})"


class OperatorToken(Token):
    pass


class PrecedenceToken(OperatorToken):
    pass


class FirstPrecedenceToken(PrecedenceToken):
    pass


class SecondPrecedenceToken(PrecedenceToken):
    pass


class ThirdPrecedenceToken(PrecedenceToken):
    pass


class MultiplyToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"MultiplyToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"MultiplyToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"


class DivideToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"DivideToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"DivideToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"


class LParenToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"LParenToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"LParenToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"


class RParenToken(FirstPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"RParenToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"RParenToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"


class AdditionToken(SecondPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"AdditionToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"AdditionToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"


class SubtractToken(SecondPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"SubtractToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"SubtractToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"


class VariableToken(Token):
    def __init__(self, ty, value, line=0, pos=0, ident=None):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"VariableToken(type: {self.type}, value: {self.value}, id: {self.ident})"

    def __repr__(self):
        return f"VariableToken(type: {self.type}, value: {self.value}, id: {self.ident} line: {self.line}, pos: {self.pos})"


class AssignmentToken(OperatorToken):
    def __init__(self, ty, value, line, pos, ident=None,):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"AssignmentToken(type: '{self.type}', operator: {self.ident} )"

    def __repr__(self):
        return f"AssignmentToken(type: '{self.type}', operator: {self.ident}, line: {self.line}, pos: {self.pos})"


class RelationalToken(ThirdPrecedenceToken):
    def __init__(self, ty, value, ident, line, pos):
        self.ident = ident
        super().__init__(ty, value, line, pos)

    def __str__(self):
        return f"RelationalToken(type: {self.type}, id: {self.ident})"

    def __repr__(self):
        return f"RelationalToken(type: {self.type}, id: {self.ident}, line: {self.line}, pos: {self.pos})"
