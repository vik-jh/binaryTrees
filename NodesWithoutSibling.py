from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



# def printNodesWithoutSibling(root) :
#     if root is None:
#         return 0
#     if root.left.data is None:
#         print(printNodesWithoutSibling(root.data))
#     else:
#         print(printNodesWithoutSibling(root.data))
#     a=printNodesWithoutSibling(root.left)
#     b=printNodesWithoutSibling(root.right)
#     if a is None:
#         return b
#     return a

def printNodesWithoutSibling(root) :
    
    if root is None:
        return 
    
    if root.right is None and root.left is not None:
        print(root.left.data,end=" ")
        
    elif root.right is not None and root.left is None:
        print(root.right.data,end=" ")
        
        
    
        
    printNodesWithoutSibling(root.left)
    printNodesWithoutSibling(root.right)































	



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

	

# Main
root = takeInput()
printNodesWithoutSibling(root)