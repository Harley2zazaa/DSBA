"""Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""
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
            return
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
        
    def insert_before(self,node, data):
        add = DataNode(data)
        pointer = self.head
        if not self.head:
            print(f"Cannot insert, "+node+" does not exist.")
            return
        if self.head.data == node:
           add.next = self.head
           self.head = add
           self.count += 1
           return
        while pointer and pointer.next:
           if pointer.next.data == node:
                add.next = pointer.next  
                pointer.next = add
                self.count += 1
                return
           pointer = pointer.next
        print(f"Cannot insert, "+node+" does not exist.")


    def delete(self,data):
        pointer = self.head
        if not self.head:
            print(f"Cannot delete, "+data+" does not exist.")
            return
        if self.head.data == data:
            if self.head.next:
                self.head = self.head.next
                self.count -= 1
                return
            else:
                self.head = None
                self.count -= 1
                return
        pointer = self.head
        while pointer and pointer.next:
            if pointer.next.data == data:
                pointer.next = pointer.next.next
                self.count -= 1
                return
            pointer = pointer.next
        print(f"Cannot delete, "+data+" does not exist.")

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
    elif condition == "B":
        mylist.insert_before(*data.split(", ")) #insert pointer /  data
    elif condition == "D":
         mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()