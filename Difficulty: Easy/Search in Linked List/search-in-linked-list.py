#User function Template for python3


''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        
        
        temp=head
        while temp:
            if temp.data==key:
                return True
            temp=temp.next
        return False