#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            return
    def detectLoop(self):
        current = self.head
        while current.next != None:
            if current.next == self.head:
                return current.data
            current = current.next
        return 0
llist = LinkedList()
llist.append(20)
llist.append(4)
llist.append(15)
llist.append(10)
print(llist.detectLoop() ,'--> No Loop')
# Create a loop for testing
llist.head.next.next.next.next = llist.head
print(llist.detectLoop(),'--> Loop detected')


# In[ ]:




