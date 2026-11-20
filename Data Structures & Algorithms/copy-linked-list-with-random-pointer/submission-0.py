"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. 交織建立複製節點：A -> A' -> B -> B'
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        
        # 2. 複製 random 指標
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # 3. 雙指標拆分新舊串列，並還原原始串列結構
        ans = head.next
        old_cur = head
        new_cur = ans
        while old_cur:
            old_cur.next = old_cur.next.next
            new_cur.next = new_cur.next.next if new_cur.next else None
            old_cur = old_cur.next
            new_cur = new_cur.next
        
        return ans