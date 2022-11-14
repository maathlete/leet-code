class Node:

    def __init__(self, label=None):

        self.label = label  
        self.count = 0
        self.children = {}

class Trie:

    def __init__(self):

        self.root = Node()

    def insert(self, word):

        trie = self.root

        for c in word:

            if c not in trie.children:

                trie.children[c] = Node(c)

            trie.children[c].count += 1
            trie = trie.children[c]

    def get_word_scores(self, word):

        trie = self.root
        count = 0

        for c in word:

            count += trie.children[c].count
            trie = trie.children[c]
            
        return(count)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()

        for word in words:

            trie.insert(word)

        word_scores = []

        for word in words:

            word_scores.append(trie.get_word_scores(word))

        return(word_scores)
