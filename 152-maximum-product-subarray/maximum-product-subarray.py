class Solution:
    def maxProduct(self, nums):
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            temp = curMax  # store old max

            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, n * temp, n * curMin)

            res = max(res, curMax)

        return res