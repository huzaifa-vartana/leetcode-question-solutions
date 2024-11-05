class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        seen = set()

        def overlap(a):
            c = Counter(a) + Counter(seen)
            return max(c.values()) > 1
            

        def helper(idx):
            if idx >= N:
                return len(seen)

            sub_str = arr[idx]
            pick = 0
            if not overlap(sub_str):
                for char in sub_str:
                    seen.add(char)
                pick = helper(idx+1)
                for char in sub_str:
                    seen.remove(char)

            return max(pick, helper(idx+1))

        return helper(0)