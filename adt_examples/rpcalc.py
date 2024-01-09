import math


class RPCalc:
    def __init__(self):
        self.stack = []

    def push(self, n):
        if isinstance(n, (int, float)):
            self.stack.append(n)
        else:
            if n == "+":
                op2, op1 = self.stack.pop(), self.stack.pop()
                self.stack.append(op1 + op2)
            elif n == "-":
                op2, op1 = self.stack.pop(), self.stack.pop()
                self.stack.append(op1 - op2)
            elif n == "*":
                op2, op1 = self.stack.pop(), self.stack.pop()
                self.stack.append(op1 * op2)
            elif n == "/":
                op2, op1 = self.stack.pop(), self.stack.pop()
                self.stack.append(op1 / op2)
            elif n == "sin":
                op = self.stack.pop()
                self.stack.append(math.sin(op))
            elif n == "cos":
                op = self.stack.pop()
                self.stack.append(math.cos(op))

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)
