
# Definition for singly-linked list.
# original answer here: https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
# couldn't figure this one out without exceeding LeetCode's maximum runtime
# traversing the linkedlist with having two speeds was definitely a great idea
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse two linked list, by using 2 speeds
        # 1 one_x, 1 two_x
        # two_x's traversal speed in 2x faster than one_x's traversal speed
        # when two_x reaches the end (having a value of None)
        # the we know that one_x is exactly at the middle of the linkedlist
        one_x = two_x = head
        while two_x and two_x.next:
            two_x = two_x.next.next
            one_x = one_x.next
            
        # traverse the back-half of `head` from one_x
        # but create a reversed linkedlist while doing so
        one_x_reversed = None
        while one_x:
            next = one_x.next
            one_x.next = one_x_reversed
            one_x_reversed = one_x
            one_x = next
        
        # after one_x_reversed is created,
        # we then compare `one_x_reversed` with the original, `head`, 
        # by traversing `head`, up until the middle
        # (or in otherwords, until `one_x_reversed` is None)
        while one_x_reversed:
            if one_x_reversed.val != head.val:
                return False
            one_x_reversed = one_x_reversed.next
            head = head.next
        
        return True