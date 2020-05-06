class AST:
    def __init__(self, data):
        self.top = data


class Node:
    def __init__(self, data):
        self.root = data
        self.lhs = None
        self.rhs = None

    def __str__(self):
        return f"Token(name: '{self.root}', left: '{self.lhs}', right: '{self.rhs}', operator: '')"


# Insert node into ast.
def insert(ast: AST, data):
    ast.top = recurs_ast(ast, ast.top, data)


# Insert node into correct position of tree.
def recurs_ast(ast: AST, node: Node, data):
    if node is None:
        node = Node(data)
    elif ast.top.root > data:
        ast.lhs = recurs_ast(ast, node.lhs, data)
    elif ast.top.root < data:
        node.rhs = recurs_ast(ast, node.rhs, data)
    return node
