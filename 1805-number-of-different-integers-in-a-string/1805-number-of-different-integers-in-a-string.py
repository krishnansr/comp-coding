class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        int_set = set()
        st = -1
        for i in range(len(word)):
            if word[i].isnumeric():
                if st == -1:
                    st = i
            else:
                if st != -1:
                    int_set.add(int(word[st:i]))
                st = -1

        if st != -1:
            int_set.add(int(word[st:]))

        return len(int_set)