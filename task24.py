class Solution:
    def extractList(self, linked_list: List[Optional[ListNode]]) -> list:

        q = linked_list
        result = []

        while (q != None):
            result.append (q.val)
            q = q.next

        return result

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        extracted_list = self.extractList(head)

        if (len(extracted_list) <= 1): return head

        evens = extracted_list[1::2]
        odds = extracted_list[::2]

        print (evens, odds)

        new_list = []
        
        i = 0
        while (i <= len(evens) and i <= len(odds)):

            if (i >= len(evens)): pass
            else: new_list.append(evens[i])
            if (i >= len(odds)): pass
            else: new_list.append(odds[i])

            i += 1

        print (new_list)

        linked_list = ListNode ()
        q = linked_list

        i = 0
        while (i != len(new_list)):
            q.val = new_list[i]

            temp = ListNode ()
            
            if (i != len(new_list)-1):
                q.next = temp
                q = q.next

            i += 1

        return linked_list

