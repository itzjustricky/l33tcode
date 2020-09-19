import math


class MinStackElement(object):
    __slots__ = ["value", "minValue", "below"]

    def __init__(self, value: int, minValue: int):
        self.value = value
        self.minValue = minValue

        self.below = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topElement = None

    def push(self, x: int) -> None:
        currMin = math.inf if self.topElement is None else self.topElement.minValue
        newMinValue = min(currMin, x)

        newStackElement = MinStackElement(x, newMinValue)
        if self.topElement is not None:
            newStackElement.below = self.topElement
        self.topElement = newStackElement

    def pop(self) -> None:
        self.topElement = self.topElement.below

    # will always be called on non-empty stacks
    def top(self) -> int:
        return self.topElement.value

    # will always be called on non-empty stacks
    def getMin(self) -> int:
        return self.topElement.minValue

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())   # return -3
    minStack.pop()
    print(minStack.top())      # return 0
    print(minStack.getMin())   # return -2
