class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        
        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in ctr.items():
            buckets[freq].append(char)

        strr = ""
        for freq in range(len(buckets) - 1, -1, -1):
            bucket = buckets[freq]
            for char in bucket:
                strr += char * freq


        return strr