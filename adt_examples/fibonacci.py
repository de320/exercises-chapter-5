

class Fib:
    def __init__(self):
        # Initialize the first two Fibonacci numbers
        self.first, self.second = 1, 2

    def __iter__(self):
        # The iterator object itself is returned by __iter__
        return self

    def __next__(self):
        # Compute the next Fibonacci number
        fib_number = self.first
        self.first, self.second = self.second, self.first + self.second
        return fib_number
