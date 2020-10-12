class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

        pass

    def insert(self, char):
        ## Add a child node in this Trie

        self.children[char] = TrieNode()

        pass

    def suffixes(self, suffix=''):
        # note, got this code from some of the help in the knowledge portal
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        path_dict = self.children
        output_list = []
        new_suffix = suffix
        for key, value in path_dict.items():
            new_suffix += key
            if value.is_word:
                output_list.append(new_suffix)
            else:
                output_list += value.suffixes(new_suffix)
            new_suffix = suffix

        return output_list

        ## Recursive function that collects the suffix for
        ## all complete words below this point


class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for letter in prefix:
            current_node = current_node.children[letter]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(" not found")
    else:
        print('')
interact(f,prefix='');