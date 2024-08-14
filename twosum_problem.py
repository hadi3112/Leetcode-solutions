
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums_dict = {}
        temp = 0
        same_encountered = 1        # if same index element added to same one then skip
        
        for i in range(len(nums)):
            temp = nums[i]
            same_encountered = 1
            for j in range(len(nums)):

                if nums[j] == 1 or nums[i] == 1:
                    print(f"nums[{i}]=  {nums[i]} nums[{j}] = {nums[j]}")
                    print(f"\n ***** same_encountered = {same_encountered}  *****\n")
                    print(sums_dict)

                if (nums[j]==nums[i] and same_encountered == 1):
                    
                    # element added to another element of same value & different index then ok
                    same_encountered+=1
                    continue

                elif same_encountered >= 1:
                    temp = nums[i]+nums[j]
                    

                    if (temp == target):
                        sums_dict[i] = temp
                        same_encountered = 1
                else:
                    temp = nums[i]+nums[j]
                    same_encountered =1

                    if (temp == target):
                        sums_dict[i] = temp
                
                
                    
        
        print(sums_dict)
        return sums_dict.keys()


sol = Solution()
print(sol.twoSum([3,2,3], 6))