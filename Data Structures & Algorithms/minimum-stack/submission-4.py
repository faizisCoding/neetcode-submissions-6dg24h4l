class MinStack:
    def __init__(self):
        self._items = []
        self.min_val = int()

    def push(self, val: int) -> None:
        if not self._items:
            self.min_val = val
        self._items.append(val)
        self.min_val = min(self.min_val, val)

    def pop(self) -> None:
        if self.min_val == self.top():
            self._items.pop()
            if self._items:
                self.min_val = self._items[0]
                for i in self._items:
                    self.min_val = min(self.min_val, i)
        else:
            self._items.pop()

    def top(self) -> int:
        return self._items[-1]

    def getMin(self) -> int:
        return self.min_val
