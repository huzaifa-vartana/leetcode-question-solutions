class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_to_name = {}
        adj = defaultdict(set)
        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                adj[email] = set(emails).union(adj[email])
                email_to_name[email] = name

        seen = set()
        def dfs(email, result):
            seen.add(email)
            result.add(email)
            for nei in adj[email]:
                if nei not in seen: 
                    dfs(nei, result)

        res = []
        for email in email_to_name.keys():
            if email not in seen:
                result = set()
                dfs(email, result)
                tmp = [email_to_name[email]] + sorted(list(result))
                res.append(tmp)

        return res

        
