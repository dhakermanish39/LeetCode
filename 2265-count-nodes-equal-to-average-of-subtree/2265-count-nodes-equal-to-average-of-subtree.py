# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        self.sm=0
        self.n=0
        def sumnode(r):
            if not r:
                return
            self.sm+=r.val
            self.n+=1
            sumnode(r.left)
            sumnode(r.right)
        sumnode(root)
        avg=self.sm/self.n
        self.avg=round(avg)
        self.rst=0
        def cnt(r):
            if not r:
                return
            if r.val>self.avg:
                self.rst+=1
            cnt(r.left)    
            cnt(r.right)
        print(self.avg)    
        cnt(root)    
        return self.rst    
        """
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rst=0

        def cnt(r):
            if not r:
                return 0,0
            lsum,lcount=cnt(r.left)
            rsum,rcount=cnt(r.right)
            sm=lsum+rsum+r.val
            n=lcount+rcount+1
            avg=sm//n
            if r.val==avg:
                self.rst+=1
            return sm,n
        cnt(root)
        return self.rst



        