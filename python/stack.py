class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack

  def __init__(self):
    self.total = 0
    self.stack = []

  def push(self, value):
    self.stack.append(value)
    self.total += 1

  def pop(self):
    self.stack = self.stack[:-1]
    self.total -= 1

  def size(self):
    return len(self.stack)


