"""Lab 03.02 - Singly Linked List (Traversal and Insert Last)"""
class DataNode:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class SinglyLinkedList:
    def __init__(self,data=None):
        self.count = 0
        self.head = data

    def insert_last(self,data):
        add = DataNode(data)
        if not self.head:
            self.head = add
        else:
            head = self.head
            while head and head.next:
              head = head.next
            head.next = add # chain node
        self.count += 1

    #def insert_front(self,data):
    #    add = DataNode(data)
    #    if not self.head:
    #        self.head = add
    #    else:
    #       head = self.head
    #       head.next = add

    #def insert_before(node, data):
    #    pass

    #def delete(data):
    #    pass

    def traverse(self):
        pointer = self.head
        if self.count == 0:
            print("This is an empty list.")
            return
        else:
          while pointer and pointer.next:
            print(pointer.data, end=" -> ")
            pointer = pointer.next
          if  pointer:
            print(pointer.data)

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    mylist.insert_last(input().strip())

  mylist.traverse()

main()