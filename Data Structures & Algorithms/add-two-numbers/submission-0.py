# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            cur.next = ListNode()
            cur = cur.next
            val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.val = val % 10
            carry = val // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next