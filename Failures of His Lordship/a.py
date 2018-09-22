class TreeNode(object):
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

def recur(A):
    if(A.val == "."):
        return None
    else:
        A.left = recur(A.left)
        A.right = recur(A.right)
        return A

def traversal(A):
    if(A):
        traversal(A.left)
        print A.val
        traversal(A.right)
    

s = "a(b(..)c(d(e(..).)f(..)))"
a = TreeNode(s[0])
c = a
for i in range(1,len(s)):
    if(s[i] == '('):
        pass
    elif(s[i] == ')'):
        c = c.parent
    else:
        if(s[i] != "."):
            if(c.left == None):
                naya = TreeNode(s[i])
                naya.parent = c
                c.left = naya
                c = c.left
            else:
                naya = TreeNode(s[i])
                naya.parent = c
                c.right = naya
                c = c.right
        else:
            if(c.left == None):
                naya = TreeNode(s[i])
                naya.parent = c
                c.left = naya
            else:
                naya = TreeNode(s[i])
                naya.parent = c
                c.right = naya

A = recur(a)
traversal(A)