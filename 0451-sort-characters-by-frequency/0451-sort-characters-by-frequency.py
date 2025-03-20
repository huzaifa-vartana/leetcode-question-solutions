class Solution:
    def frequencySort(self, s: str) -> str:
        ctr = Counter(s)
        
        sorted_ctr = {k: v for k, v in sorted(ctr.items(), key=lambda item: item[1], reverse=True)}
        
        strr = ""
        for char, freq in sorted_ctr.items():
            strr += char * freq
        return strr
