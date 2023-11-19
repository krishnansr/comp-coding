class Solution:
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Comments if needed https://leetcode.com/problems/word-search/discuss/3183331/79.-Word-Search-with-step-by-step-explanation
        
        rows = len(board)
        cols = len(board[0])

        def backtrack(r: int, c: int, ind: int) -> bool:
            if not (0 <= r < rows and 0 <= c < cols and board[r][c] == word[ind]):
                return False

            if ind == len(word) - 1:
                # finished building the word
                return True

            # Found a match at current index.
            tmp = board[r][c]
            board[r][c] = '~'  # Explored, so set to a random character.
            for dx, dy in self.moves:
                new_r = r + dx
                new_c = c + dy
                if backtrack(new_r, new_c, ind + 1):
                    return True
            board[r][c] = tmp  # Didn't find any match, return char.
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False
                