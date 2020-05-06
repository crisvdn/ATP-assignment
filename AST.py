class Node:
    def __init__(self, data):
        self.root = data
        self.lhs = None
        self.rhs = None

    def __str__(self):
        return f"Token(name: '{self.root}', left: '{self.lhs}', right: '{self.rhs}', operator: '')"


class AST:
    def __int__(self, data):
        self.top = data

    def insert(self, data):
        self.top = self.recursAST(self.top, data)


def recursAST(ast: AST, node: Node, data):
    if node is None:
        node = Node(data)
    elif ast.top.root > data:
        ast.lhs = recursAST(ast, node.lhs, data)
    elif ast.top.root < data:
        node.rhs = recursAST(ast, node.rhs, data)
    return node