class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist_map = OrderedDict()
        
        for word in arr:
            if word in dist_map:
                dist_map[word] = -1
            else:
                dist_map[word] = 1
        
        i = 0
        for key, val in dist_map.items():
            if val == 1:
                i += 1
                if i == k:
                    return key
        
        return ''