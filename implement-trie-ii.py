class Node:

    def __init__(self, prefix=None):

        self.occurrences_as_prefix = 0
        self.occurrences_as_full_word = 0
        
        self.prefix = prefix
        self.children = {}

class Trie:

    def __init__(self):
        
        self.root = Node()

    def insert(self, word: str) -> None:

        trie = self.root

        prefix = ''

        for c in word:
        
            prefix += c

            if prefix not in trie.children:

                trie.children[prefix] = Node(prefix)

            trie.occurrences_as_prefix += 1
            trie = trie.children[prefix]
        
        trie.occurrences_as_full_word += 1
        trie.occurrences_as_prefix += 1

    def countWordsEqualTo(self, word: str) -> int:

        trie = self.root

        prefix = ''

        for c in word:

            prefix += c

            if prefix not in trie.children:
        
                return(0)
            
            else:

                trie = trie.children[prefix]
        
        return(trie.occurrences_as_full_word)

    def countWordsStartingWith(self, prefix: str) -> int:
        
        trie = self.root

        pre = ''

        for c in prefix:

            pre += c

            if pre not in trie.children:

                return(0)

            trie = trie.children[pre]
        
        return(trie.occurrences_as_prefix)
        
    def erase(self, word: str) -> None:

        trie = self.root

        prefix = ''

        for c in word:

            prefix += c

            trie.occurrences_as_prefix -= 1
            
            trie = trie.children[prefix]

        trie.occurrences_as_full_word -= 1
        trie.occurrences_as_prefix -= 1
