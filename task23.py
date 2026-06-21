class Solution:
    def extractList(self, linked_list: List[Optional[ListNode]]) -> list:

        q = linked_list
        result = []

        while (q != None):
            result.append (q.val)
            q = q.next

        return result


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        all_linked_lists = []

        for i in range (len(lists)):
            all_linked_lists += self.extractList(lists[i])

        all_linked_lists.sort()
        
        if (all_linked_lists == []): return None

        merged_list = ListNode ()
        q = merged_list

        i = 0
        while (i != len(all_linked_lists)):
            q.val = all_linked_lists[i]

            temp = ListNode ()
            
            if (i != len(all_linked_lists)-1):
                q.next = temp
                q = q.next

            i += 1

        return merged_list