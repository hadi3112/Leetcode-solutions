from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse current node's pointer
            prev = current            # Move prev and current one step forward
            current = next_node
        return prev  # New head of the reversed list