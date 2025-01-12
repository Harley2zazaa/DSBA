"""Lab 04.03 – Binary Search Tree (Traversals)"""
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
        print("Preorder: ", end="")
        self.re_preorder(pointer)
        print()

    def re_preorder(self,pointer):
        if not pointer:
            return
        print("-> " + str(pointer.data), end=" ")
        self.re_preorder(pointer.left)
        self.re_preorder(pointer.right)
    
    def inorder(self):
        pointer = self.root
        print("Inorder: ", end="")
        self.re_inorder(pointer)
        print()
    
    def re_inorder(self,pointer):
        if not pointer:
            return
        self.re_inorder(pointer.left)
        print("-> " + str(pointer.data), end=" ")
        self.re_inorder(pointer.right)

    def postorder(self):
        pointer = self.root
        print("Postorder: ", end="")
        self.re_postorder(pointer)
        print()
    
    def re_postorder(self,pointer):
        if not pointer:
            return
        self.re_postorder(pointer.left)
        self.re_postorder(pointer.right)
        print("-> " + str(pointer.data), end=" ")

    def find_min(self):
        pointer = self.root
        if self.is_empty(self):
            return "None"
        else:
            return self.re_min(pointer)

    def re_min(self,pointer):
        if not pointer.left:
            return pointer.data
        return self.re_min(pointer.left)

    def find_max(self):
        pointer = self.root
        if self.is_empty(self):
            return "None"
        else:
            return self.re_max(pointer)

    def re_max(self,pointer):
        if not pointer.right:
            return pointer.data
        return self.re_max(pointer.right)
    
    def delete(self,data):
        self.root = self.re_del(self.root, data)

    def re_del(self,node,data):
        if node is None :
            print("Delete Error, "+str(data)+" is not found in Binary Search Tree.")
            return None
        if data < node.data:
            node.left = self.re_del(node.left, data)
        elif data > node.data:
            node.right = self.re_del(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_values = self.re_max(node.left)
                node.data = min_values
                node.left = self.re_del(node.left, min_values)
        return node


    def is_empty(node):
        if node.root is None or not node.root.data:
            return True
        return False

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            self.preorder()
            self.inorder()
            self.postorder()

def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()
