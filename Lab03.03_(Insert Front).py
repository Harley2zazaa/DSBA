"""Lab 03.03 - Singly Linked List (Insert Front)"""
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
            while head.next:
              head = head.next
            head.next = add # chn node
        self.count += 1

    def insert_front(self,data):
        add = DataNode(data)
        if not self.head:
            self.head = add
        else:
            add.next = self.head
            self.head = add
        self.count += 1
        
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
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    # elif condition == "B":
    #     mylist.insert_before(*data.split(", "))
    # elif condition == "D":
    #     mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()