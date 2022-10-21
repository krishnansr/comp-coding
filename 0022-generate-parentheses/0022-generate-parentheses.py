class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []

        def dfs(left_sum, right_sum, path):
            if left_sum < right_sum:
                return
            if left_sum == right_sum == n:
                combinations.append(path)
                return
            if left_sum < n:
                dfs(left_sum + 1, right_sum, path + '(')
            if right_sum < n:
                dfs(left_sum, right_sum + 1, path + ')')

        dfs(0, 0, '')
        return combinations