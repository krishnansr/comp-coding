class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        result = float("inf")
        
        edge_maps = [set() for _ in range(n)]
        for (fr, to) in edges:
            edge_maps[fr - 1].add(to - 1)
            edge_maps[to - 1].add(fr - 1)
            
        node_degree = [len(edge_maps[i]) for i in range(n)]
        for fr1, fr1_friends in enumerate(edge_maps):
            if len(fr1_friends) > 1:
                for fr2 in fr1_friends:
                    for fr3 in fr1_friends & edge_maps[fr2]:
                        out_friends = node_degree[fr1] + node_degree[fr2] + node_degree[fr3] 
                        result = min(result, out_friends - 6)
                        edge_maps[fr3].discard(fr2)
                        edge_maps[fr3].discard(fr1)

        return result if result != float("inf") else -1