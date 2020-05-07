from typing import List, TypeVar
import interpreter as i

A = TypeVar('A')
RESULT = TypeVar('RESULT')

class AST:
    def __init__(self, data=None):
        self.top = data


class Node:
    def __init__(self, data):
        self.root = data
        self.lhs = None
        self.rhs = None

    def __str__(self):
        return f"Token(name: '{self.root.__repr__()}', left: '{self.lhs}', right: '{self.rhs}', operator: '')"


# Insert node into ast.
def insert(ast: AST, data):
    ast.top = recurs_ast(ast, ast.top, data)


# Insert node into correct position of tree.
def recurs_ast(ast: AST, data: List[A]) -> RESULT:
    