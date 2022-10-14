from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        nodes = [head]
        while head.next is not None:
            nodes.append(head.next)
            head = head.next
            
        return nodes[int((len(nodes)-1) / 2) + ((len(nodes)-1) % 2)]