"""Lab 04.01 - Create BSTNode"""
class BSTNode:
    def __init__(self,data:int=None):
        self.data = data
        self.left = None
        self.right = None

def main():
    p_new = BSTNode(int(input()))
    print(p_new.data)
    print(p_new.left)
    print(p_new.right)

main()