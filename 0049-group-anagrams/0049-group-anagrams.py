class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash = defaultdict(list)
        for idx, word in enumerate(strs):
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            hash[tuple(count)].append(word)   


        return list(hash.values())