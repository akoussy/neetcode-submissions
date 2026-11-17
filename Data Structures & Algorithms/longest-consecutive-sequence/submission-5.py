class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        curr=1
        largest=1
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i+1]-1==nums[i]:
                curr+=1
                largest=max(largest,curr)
            else:
                curr=1
        return largest
        