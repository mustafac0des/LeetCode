# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1=[]
        node2=[]

        q=l1

        while(q!=None):
            node1.append(q.val)
            q=q.next

        q=l2

        while(q!=None):
            node2.append(q.val)
            q=q.next

        node1=node1[::-1]
        node2=node2[::-1]

        num1=""
        num2=""

        for i in range(len(node1)):
            num1=num1+str(node1[i])

        for i in range(len(node2)):
            num2=num2+str(node2[i])

        result=int(num1)+int(num2)
        result=str(result)

        node3=list(result)
        node3=node3[::-1]

        print(node3)

        l3=ListNode(int(node3[0]), None)
        q=l3
        
        for i in range(len(node3)):
            if (i==0): continue 
            temp=ListNode(int(node3[i]), None)
            q.next=temp
            q=q.next

        return l3

