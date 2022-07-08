# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listArray = []
        cur = head
        while(cur != None):
            listArray.append(cur.val)
            cur = cur.next

        return listArray == list(reversed(listArray))
