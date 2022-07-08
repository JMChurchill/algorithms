# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # get length
        length = 0
        cur = head
        while(cur != None):
            length = length + 1
            cur = cur.next
        if(length == 1):
            return head
        # get middle
        cur = head
        middle = length // 2
        for i in range(length):
            cur = cur.next
            if i == middle-1:
                return cur
