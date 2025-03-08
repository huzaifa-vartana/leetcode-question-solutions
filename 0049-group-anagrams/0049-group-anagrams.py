class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # # n * (xlgx)
        # for idx, word in enumerate(strs):
        #     strs[idx] = ''.join(sorted(word))

        # # nlgn
        # strs.sort()
        # print(strs)

        hash = defaultdict(list)
        for idx, word in enumerate(strs):
            d = Counter(word)
            ctr = dict(sorted(d.items()))
            hash[str(ctr)].append(idx)   

        res = []
        for key, items in hash.items():
            tmp = []
            for item in items:
                tmp.append(strs[item])
            res.append(tmp)
        return res