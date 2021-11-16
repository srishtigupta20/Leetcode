"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None: return None
        
        leftMost = root
        while leftMost.left:
            head = leftMost
            leftMost = head.left
            while head:
                head.left.next = head.right
                if head.next != None:
                    head.right.next = head.next.left
                head = head.next
        return root
