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
            
    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """   
        curr_node = self.root
        
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.end_char  # to differentiate b/w apple and app.
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that has the given prefix.
        """ 
        curr_node = self.root
        
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True  # don't differentiate b/w apple and app.
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)