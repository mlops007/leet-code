class Solution:
  def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        my_dict = {}
        for i in range(0,len(nums)):
            print(f"Instance : {i} \t dict --> {my_dict}")
            comp = target - nums[i]
            print(f"Target : {target} \t Element : {nums[i]} \t Comp : {comp}")
            if comp in my_dict:                
                return [my_dict[comp], i]
            my_dict[nums[i]] = i

nums = [2,7,11,4]
target = 13

s = Solution.twoSum(Solution(),nums,target)
print(s)

