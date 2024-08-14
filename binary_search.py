
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        found = 0 
        i = 0
        mid_index = int(len(nums)/2)

        mid_elem = nums[mid_index]
        print(mid_elem)

        bucket1 = nums[0:mid_index]
        bucket2 = nums[mid_index:]

        print(bucket1)
        print(bucket2)

        if mid_elem == target:
            return mid_index
        elif (target < mid_elem):
            
            print("target smaller")
            while found==0 and i<mid_index:
                if bucket1[i] == target:
                    found=1
                    print("found")
                    return i
                else:
                    i+=1
        elif (target > mid_elem):
            print("target larger")
            while found==0 and i<len(bucket2):
                if bucket2[i] == target:
                    found=1
                    return mid_index+i
                else:
                    i+=1
        
        return -1

     
        
    
sol = Solution()
print(sol.search([-1,0,5], 5))