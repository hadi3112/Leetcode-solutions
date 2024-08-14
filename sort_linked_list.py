class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        # dummy = ListNode()
        # temp = ListNode()
        # dummy = head
        # temp_val = 0
        # list_length = 0
        
        # #first pass
        # while dummy is not None:
        #     temp = dummy.next
            
        #     # Ensure temp is not None before accessing temp.val
        #     if temp is not None and temp.val < dummy.val:
        #         temp_val = dummy.val
        #         dummy.val = temp.val
        #         temp.val = temp_val
                
        #     dummy = dummy.next
        #     list_length += 1


        # # reset stuff
        # dummy = ListNode()
        # temp = ListNode()
        # dummy = head
        # temp_val = 0
        # passes_left = 3 * list_length

        # # all other passes
        # while dummy is not None and passes_left != 0:
        #     temp = dummy.next
            
        #     # Ensure temp is not None before accessing temp.val
        #     if temp is not None and temp.val < dummy.val:
        #         temp_val = dummy.val
        #         dummy.val = temp.val
        #         temp.val = temp_val
                
        #     dummy = dummy.next
        #     passes_left -= 1
            
        # spitballing
        dummy = ListNode()
        dummy = head
        arr = []

        while dummy!=None:
            arr.append(dummy.val)
            dummy = dummy.next
        arr.sort()
        print(arr)
        dummy = ListNode()
        dummy = head    
        index = 0    

        while dummy!=None:
            dummy.val = arr[index]
            index+=1
            dummy = dummy.next

        return head
    
sol = Solution()
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print(sol.sortList(head))