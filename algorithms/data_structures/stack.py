"""
    Stack
    -----
    A stack or LIFO (last in, first out) is an abstract data type that serves
    as a collection of elements, with two principal operations: push, which
    adds an element to the collection, and pop, which removes the last element
    that was added.

    Operations:
    is_empty()
    peek()
    pop()
    push()
    size()
     

    Pseudo Code: https://en.wikipedia.org/wiki/Stack_%28abstract_data_type%29
"""


class Stack:

    def __init__(self):
        self.stack_list = []
        self.size = 0


    def is_empty(self):
        """
        Return True if stack is empty 

        Time Complexity:  O(1)
        """
        return self.size == 0
    
     def peek(self):
        """
        Return the item currently on top of the stack

        Time Complexity:  O(1)
        """
        return self.stack_list[self.size-1]
     

    def pop(self):
        """
        Remove and return element on top of stack

        Time Complexity:  O(1)

        Error will be thrown if size is 0
        """
        self.size -= 1 
        return self.stack_list.pop()

    def push(self, value):
        """
        Add element to top of stack

        Time Complexity:  O(1)
        """
        self.stack_list.append(value)
        self.size += 1

  
    def size(self):
        """
        Return size of stack

        Time Complexity:  O(1)
        """
        return self.size
    
   