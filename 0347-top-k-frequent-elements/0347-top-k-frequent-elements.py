class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        ctr = Counter(nums)
        for num, freq in ctr.items():
            buckets[freq].append(num)

        res = []
        for bucket in reversed(buckets):
            if bucket:
                for num in bucket:
                    res.append(num)
                
                    k -=1
                if k <= 0: break

        return res