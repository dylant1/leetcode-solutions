class Solution:
    def groupAnagrams(self, strs):
        
        m = {}
        
        for string in strs:
            if "".join(sorted(string)) not in m:
                m["".join(sorted(string))] = [string]
            else:
                m["".join(sorted(string))].append(string)
        res = []
        for k, value in m.items():
            res.append(value)
            
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
        