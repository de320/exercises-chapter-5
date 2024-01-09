

class Deque:
    def __init__(self, size):
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def append(self, x):
        if self.count == len(self.buffer):
            raise IndexError("Deque is full")
        self.buffer[self.tail] = x
        self.tail = (self.tail + 1) % len(self.buffer)
        self.count += 1

    def appendleft(self, x):
        if self.count == len(self.buffer):
            raise IndexError("Deque is full")
        self.head = (self.head - 1) % len(self.buffer)
        self.buffer[self.head] = x
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError("Deque is empty")
        self.tail = (self.tail - 1) % len(self.buffer)
        x = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.count -= 1
        return x

    def popleft(self):
        if self.count == 0:
            raise IndexError("Deque is empty")
        x = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % len(self.buffer)
        self.count -= 1
        return x

    def peek(self):
        if self.count == 0:
            raise IndexError("Deque is empty")
        return self.buffer[self.tail - 1]

    def peekleft(self):
        if self.count == 0:
            raise IndexError("Deque is empty")
        return self.buffer[self.head]

    def __len__(self):
        return self.count

    def __iter__(self):
        i = self.head
        for _ in range(self.count):
            yield self.buffer[i]
            i = (i + 1) % len(self.buffer)
