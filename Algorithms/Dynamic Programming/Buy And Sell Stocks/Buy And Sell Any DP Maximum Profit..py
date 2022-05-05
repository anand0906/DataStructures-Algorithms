class Node:
    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.word = None
        self.freq = 0

class PrefixTree:
    def __init__(self, words):
        self.root = Node(None)
        for word in words:
            self.insert(word)
        
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                child = Node(char)
                curr.children[char] = child
            else:
                child = curr.children[char]
            curr = child
        curr.word = word
        curr.freq += 1   
def getAllPairs(strs):
    rstrs = [x[::-1] for x in strs]
    root = PrefixTree(rstrs).root
    res = []
    dfs(root, dict(), res)
    return res
    
def dfs(curr, sf, res):
    if curr.word is not None and len(sf) > 0:
        for word, freq in sf.items():
            res += [[curr.word[::-1], word[::-1]] for _ in range(curr.freq * freq)]
    if curr.freq > 1:
        res += [[curr.word[::-1], curr.word[::-1]] for _ in range(curr.freq * (curr.freq-1) // 2)]
    if curr.word is not None:
        sf[curr.word] = curr.freq
    for child in curr.children.values():
        dfs(child, sf, res)
    if curr.word in sf:
        del sf[curr.word]
s=input()
k=getAllPairs(["cba", "a", "a","b", "ba", "ca"])
print(k)
