
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        my_dict = {}
        for elem in nums:
            my_dict[elem] = 0
        
        for i in range(len(nums)):
            if nums[i] in my_dict.keys():
                my_dict[nums[i]] += 1
        print(my_dict)
        most_occuring_key = max(my_dict, key = my_dict.get)
        print(f"most_occuring_key = {most_occuring_key}")
 
        if any(v > 1 for k, v in my_dict.items()) == 1:
            return most_occuring_key
        else:
            return max(my_dict.keys())


        # my_dict = {}
        # for elem in nums:
        #     if elem not in my_dict.keys():
        #         elem_count = 1
        #         my_dict[elem] = elem_count
        #         print(my_dict)
        #         prev_elem = elem
                
        #     else:
        #         current_elem = elem

        #         if prev_elem == current_elem:
        #             elem_count = elem_count + 1
        #             my_dict[elem] = elem_count
        #             print(my_dict)
                

        
        
        # most_occuring_key = max(my_dict, key = my_dict.get)
        # print(f"most_occuring_key = {most_occuring_key}")
 
        # if any(v > 1 for k, v in my_dict.items()) == 1:
        #     return most_occuring_key
        # else:
        #     return max(my_dict.keys())
    
sol = Solution()
print(sol.majorityElement([1,1, 0, 0,0,1, 1]))