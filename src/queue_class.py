"""
QUEUE REALIZATION
"""

class Queue():
    def __init__(self) -> None:
        self._queue = []

    def enque(self, val):
        self._queue.append(val)

    def deque(self):
        if len(self._queue) != 0:
            return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0