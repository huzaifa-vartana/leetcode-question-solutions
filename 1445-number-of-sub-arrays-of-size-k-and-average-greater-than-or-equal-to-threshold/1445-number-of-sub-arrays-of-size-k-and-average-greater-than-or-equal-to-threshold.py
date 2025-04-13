class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        """
        arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
        """
        N, l, ans, summ = len(nums), 0, 0, 0

        for r in range(N):

            summ += nums[r]

            # check and handle in-valid window of size K
            if r - l + 1 > k:
                summ -= nums[l]
                l += 1

            # this is valid window
            if r - l + 1 == k and summ / k >= threshold: ans += 1


        return ans