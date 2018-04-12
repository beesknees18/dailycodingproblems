class Node:
    def __init__(self, value):
        self.val = value
        self.leftchild = None
        self.rightchild = None

def create_tree(preorder, inorder):
    if len(preorder) == 0:
        return
    
    print(preorder)
    # print(inorder)
    n = Node(preorder[0])

    inorderIndex = inorder.index(preorder[0])

    n.leftchild = create_tree(preorder[1: inorderIndex + 1], inorder[:inorderIndex])
    n.rightchild = create_tree(preorder[inorderIndex + 1: inorderIndex + 1+ len(inorder[:inorderIndex])], inorder[inorderIndex + 1:]) 

    return n

def print_inorder(n):
    if n:
        print(n.val)
        print(n.leftchild)
        print(n.rightchild)
        print_inorder(n.leftchild)
        print_inorder(n.rightchild)

result = create_tree(['a','b','d','e','c','f','g'], ['d','b','e','a','f','c','g'])
print_inorder(result)