class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        w_sum = sum(nums[:k])   
        w_max = w_sum

        for i in range(k, len(nums)):  
            w_sum = w_sum + nums[i] - nums[i - k]   
            w_max = max(w_max, w_sum)   

        return w_max / k   