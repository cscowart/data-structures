class Queue:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue

  def __init__(self):
    self.q = []
    self.total = 0

  def enqueue(self, value):
    # write your code to add data to the Queue following FIFO and return the Queue
    self.q.append(value)
    self.total += 1

  def dequeue(self):
    self.q = self.q[1:]
    self.total -= 1
    # write your code to removes the data to the Queue following FIFO and return the Queue
    

  def size(self):
    # write your code that returns the size of the Queue
    return self.total

