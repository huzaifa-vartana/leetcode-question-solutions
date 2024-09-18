class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        # bucket sort implementation
        for num, freq in counter.items():
            buckets[freq].append(num)

        res = []

        for bucket in reversed(buckets):
            if len(res) >= k:
                break
            res.extend(bucket)

        return res
