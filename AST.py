from typing import List, TypeVar
import Tokens

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
def insert(ast_cur_node: Node, tokens:List[Tokens.Token]) -> AST:
    ast_cur_node.value = tokens[1]
    ast_cur_node.lhs = Node()
    ast_cur_node.rhs = Node()
    ast_cur_node.lhs.value = tokens[0]
    ast_cur_node.rhs.value = tokens[2]

def print_ast(root: Node):
    if root:
        print_ast(root.lhs)
        print(root.value)
        print_ast(root.rhs)

# Insert node into correct position of tree.
#def recurs_ast(ast: AST, current_node:Node, data: List[A]) -> RESULT: