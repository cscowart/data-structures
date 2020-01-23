class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList

  def __init__(self):    
    self.head = Node(None)     
    self.next = None # maybe take out later  
    self.length = 0

  def add(self, data):
    # write your code to ADD an element to the Linked List
    if self.head.data == None: # only one element in list
      self.head.data = data
      self.length += 1
    else: # multiple elements in list
      currentNode = self.head
      while currentNode.next != None:
        currentNode = currentNode.next
      currentNode.next = Node(data)
      self.length += 1
        
  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    currentNode = self.head

    if self.head.data == data:
      self.head.data = self.head.next.data
      self.head.next = self.head.next.next
      return

    while currentNode.next.data != data: # finds node before node to be deleted
      currentNode = currentNode.next 
    currentNode.next = currentNode.next.next

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    currentNode = self.head
    while currentNode.data != element_to_get:
      currentNode = currentNode.next
    return currentNode

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  
  def __init__(self, data):
    self.data = data
    self.next = None
