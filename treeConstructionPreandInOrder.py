from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



        
def buildTree(preOrder, inOrder, n) :
	#Your code goes here
    if len(preOrder) == 0:
        return None
    rootdata = preOrder[0]
    root = BinaryTreeNode(rootdata)
    for i in range(len(inOrder)):
        if inOrder[i] == rootdata:
            rootindex = i
            break
    if rootindex == -1:
        return None
    leftinOrder = inOrder[0:rootindex]
    rightinOrder = inOrder[rootindex + 1:]
    
    lenleftsubtree = len(leftinOrder)
    
    leftpreOrder = preOrder[1:lenleftsubtree + 1]
    rightpreOrder = preOrder[lenleftsubtree + 1:]
    
    leftChild = buildTree(leftpreOrder, leftinOrder, n)
    rightChild = buildTree(rightpreOrder, rightinOrder, n)
    
    root.left = leftChild
    root.right = rightChild

    return root
    
    
def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)