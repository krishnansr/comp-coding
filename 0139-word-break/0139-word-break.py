# Using tries (prefix-trees) from https://leetcode.com/problems/implement-trie-prefix-tree/
class TrieNode:
    def __init__(self):
        # We're not storing the value explicitly as that'll rememebered in the children dict.
        self.children = dict()
        self.end_char = False

class Trie:
    # Trie (Prefix trees) are very useful for checking prefixes very quickly.
    # Also useful for any autocomplete, spellchecker usecases.
    
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        
        for char in word:
            if char not in curr_node.children:
                # Adding a new chat at current level
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_char = True  # to mark end of word.

    def search_parts(self, word: str, st: int, end: int) -> List[int]:
        """
        Returns True if the word is in the trie.
        """   
        curr_node = self.root
        
        end_of_word = []
        for i in range(st, end + 1):
            char = word[i]
            if char not in curr_node.children:
                break
            curr_node = curr_node.children[char]
            if curr_node.end_char:
                end_of_word.append(i)
        
        return end_of_word    
        

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DFS solution (using Tries) + cache -> Time O(N^3 + M)
        # Better O(N^2) solutions available in https://leetcode.com/problems/word-break/discuss/1455100/Python-3-solutions%3A-Top-down-DP-Bottom-up-DP-then-Optimised-with-Trie-Clean-and-Concise
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        @lru_cache(None)
        def search_trie(st, end):
            parts = trie.search_parts(s, st, end)
            for part in reversed(parts):
                if part == len(s) - 1 or search_trie(part + 1, end):
                    return True

        return search_trie(st=0, end=len(s) - 1)
