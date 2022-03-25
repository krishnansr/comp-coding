class Solution:
    def _update_dist(self, s, c, short_dist, direction):
        _dist = len(s)
        for i in range(_dist)[::direction]:
            if s[i] == c:
                _dist = 0
            short_dist[i] = min(short_dist[i], _dist)
            _dist += 1
    
    def shortestToChar(self, s: str, c: str) -> List[int]:
        short_dist = [len(s) - 1] * len(s)
        
        self._update_dist(s, c, short_dist, direction=1)
        self._update_dist(s, c, short_dist, direction=-1)
        return short_dist