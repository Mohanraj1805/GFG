"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        # Code here
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev#switching to the NULL pointer
            prev=cur
            cur=nxt
        return prev