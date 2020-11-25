# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time complexity - O(n+m) # n is the length of linkedlist 1 and m is the length of linkedlist 2.
# Space complexity - O(n)
# Did this solution run on leetcode? - yes
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeSet = set()
        while headA:            
            # add the current node to the node set.
            nodeSet.add(headA)            
            headA = headA.next
        
        # Check whether the node is present in node set, return the current node. 
        # This is the point of intersection.
        while headB:
            if headB in nodeSet:
                return headB
            headB = headB.next

# Time complexity - O(n+m) # n is the length of linkedlist 1 and m is the length of linkedlist 2.
# Space complexity - O(1)
# Did this solution run on leetcode? - yes
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        self.headA, self.headB = headA, headB
        
        p1, p2 = self.traverse(headA, headB)
        p1, p2 = self.traverse(p1, p2)
        
        # return the location of the intersection
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        
        return None 
            
    def traverse(self, p1, p2):
        # traverse both the lists together.
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            
        if not p1:
            p1 = self.headB
        if not p2:
            p2 = self.headA
        return p1, p2


# Time complexity - O(n+m) # n is the length of linkedlist 1 and m is the length of linkedlist 2.
# Space complexity - O(1)
# Did this solution run on leetcode? - yes
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # find length of linked lists.
        lenA = self.__find_length(headA)
        lenB = self.__find_length(headB)
        
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
            
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        while headA!=headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
    def __find_length(self, node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length
        