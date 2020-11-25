# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity - O(n)
# Space complexity - O(n) # because of using extra stack space.
# Did this solution run on leetcode? - yes
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # edge cases
        if not head:
            return head
        if not head.next:
            return head
        
        # Time complexity - O(n)
        slowptr, fastptr = head, head.next
        # find the middle of the list
        while fastptr and fastptr.next:
            slowptr = slowptr.next          # jump 1 node
            fastptr = fastptr.next.next     # jump 2 nodes
        
        # Time complexity - O(n)
        # Space complexity - O(n)
        # fetch the second half of the linked list.
        node_stack = []
        temp = slowptr.next     # begin from the second half of the linked list.
        slowptr.next = None     # point the next pointer of the first half of the linked list to None.
        slowptr = temp          
        while slowptr:
            temp = slowptr.next
            slowptr.next = None
            node_stack.append(slowptr)
            slowptr = temp      # point to the next node
        
        # Time complexity - O(n)
        # modified list node
        slowptr = head                                      
        while node_stack:
            temp = slowptr.next                             
            # point to the node from the node stack
            slowptr.next = node_stack.pop()                 
            slowptr.next.next = temp                        
            slowptr = slowptr.next.next                     
        
        return head
            
            
# Time complexity - O(n)
# Space complexity - O(1) 
# Did this solution run on leetcode? - yes
class Solution:
    def reorderList(self, head: ListNode) -> None:   
        if not head:
            return head
        
        # slowptr points to the middle of the list.
        slowptr, fastptr = head, head
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
        
        # reverse the second half of the linked list.
        secondhead = self.reverseLinkedList(slowptr)
        
        # separate the first and second part of linked list.
        # linked list: 1->2->3->4->5->6
        # first: 1->2->3->4
        # second: 6->5->4
        # step1: 1->6->2
        # step2: 1->6->2->5->3->4
        slowptr.next = None
        merged = head                           # 1
        while secondhead.next:
            # second linked list
            temp = merged.next                  # 2
            merged.next = secondhead            # 1->5
            
            # first linked list
            temp2 = secondhead.next
            merged.next.next = temp                  # 1->5->2
            merged = merged.next.next                # pts to 2
            
            secondhead = temp2
        
        return head
        
        
    def reverseLinkedList(self, node: ListNode) -> ListNode:
        if node.next is None:
            return node
        
        head = self.reverseLinkedList(node.next)
         # reversal step
        node.next.next = node   # point the next node to the current node
        node.next = None        # point the next of the current node to None
                                # this will be updated to the previous node 
        
        return head