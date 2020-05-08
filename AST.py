from typing import List, TypeVar

A = TypeVar('A')
RESULT = TypeVar('RESULT')

class AST:
    def __init__(self, data=None):
        self.top = Node()

    def __str__(self):
        return f"AST(top: '{self.top.__str__()}')"

    __repr__ = __str__


class Node:
    def __init__(self):
        self.value = None
        self.lhs = None
        self.rhs = None


    def __str__(self):
        return f"Node(value: {self.value.__repr__()}, \nlhs: {self.lhs}, \nrhs: {self.rhs})"


    def __repr__(self):
        return f"Node(value: {self.value.__repr__()}, \nlhs: {self.lhs}, rhs: {self.rhs})"


# Insert node into ast.
def insert(ast: AST, ast_cur_node: Node, data) -> AST:
    if len(data) == 0:
        print("printing ast:", ast)
        print("")
        print("returning")
        return ast
    elif ast_cur_node.value is not None:
        ast = insert(ast, ast_cur_node, data[2:])
    else:
        ast_cur_node.value = data[1]
        ast_cur_node.lhs = data[0]
        ast_cur_node.rhs = data[2]
        ast = insert(ast, ast_cur_node, data[2:])



# Insert node into correct position of tree.
#def recurs_ast(ast: AST, current_node:Node, data: List[A]) -> RESULT: