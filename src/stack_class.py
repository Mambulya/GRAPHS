"""
STACK REALIZATION
"""

class Stack():
    def __init__(self) -> None:
        self._stack = []

    def pop(self) -> None:
        if len(self._stack) != 0:
            return self._stack.pop()

    def push(self, elem) -> None:
        self._stack.append(elem)

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def __repr__(self) -> str:
        return repr(self._stack)

    def print_stack(self):
        print("[", end = "")
        for el in self._stack:
            if self._stack.index(el) != len(self._stack) - 1:
                print(el, end=", ")
            else:
                print(el, end = "")
        print("]")
