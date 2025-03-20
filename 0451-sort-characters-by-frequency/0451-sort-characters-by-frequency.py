class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        
        heap = [(-freq, char) for char, freq in ctr.items()]
        heapq.heapify(heap)
        
        strr = ""
        while heap:
            freq, char = heapq.heappop(heap)
            strr += char * -(freq)
        return strr
