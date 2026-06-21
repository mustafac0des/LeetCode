class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p = list1
        q = list2

        l1 = []
        l2 = []

        while (p != None):
            l1.append(p.val)
            p = p.next

        while (q != None):
            l2.append(q.val)
            q = q.next

        sorted_list = l1 + l2
        sorted_list.sort()

        if (sorted_list == []): return None

        merged_list = ListNode ()
        r = merged_list

        i = 0
        while (i != len(sorted_list)):
            r.val = sorted_list[i]

            temp = ListNode ()
            
            if (i != len(sorted_list)-1):
                r.next = temp
                r = r.next

            i += 1

        return merged_list

