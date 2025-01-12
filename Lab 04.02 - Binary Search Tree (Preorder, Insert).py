"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""
class BSTNode:
    def __init__(self,data:int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = BSTNode()

    def insert(self,data,node=None):
        if self.root.data == None:
            self.root.data = data
            return
        elif data and node:
            if data < node.data:
                if node.left is None:
                    node.left = BSTNode(data)
                else:
                    self.insert(data,node.left)
            else:
                if node.right is None:
                    node.right = BSTNode(data)
                else:
                    self.insert(data,node.right)
        else:
            if data < self.root.data:
                if self.root.left is None:
                    self.root.left = BSTNode(data)
                else:
                    self.insert(data,self.root.left)
            else:
                if self.root.right is None:
                    self.root.right = BSTNode(data)
                else:
                    self.insert(data,self.root.right)

    def preorder(self):
        pointer = self.root
        self.re_preorder(pointer)
        print()

    def re_preorder(self,pointer):
        if not pointer:
            return
        print("-> " + str(pointer.data), end=" ")
        self.re_preorder(pointer.left)
        self.re_preorder(pointer.right)
        

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
    
  print("Preorder: ", end="")
  my_bst.preorder()

main()