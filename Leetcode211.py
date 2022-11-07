class WordDictionary(object):

    def __init__(self):
        self.prefix_tree={}


    def addWord(self, word):
        tree = self.prefix_tree
        for a in word:
            tree = tree.setdefault(a, {})
        tree["#"] = '#'

    def search(self, word):

        def dfs(tree,index):
            if index==len(word):
                if '#' in tree:
                    return True
            else:
                if word[index]=='.':
                    for i in tree:
                        if i!='#':
                            if dfs(tree[i],index+1):
                                return True
                            # else:
                            #     return False
                elif word[index] in tree:
                    if dfs(tree[word[index]],index+1):
                        return True
                return False

        return dfs(self.prefix_tree,0)


{u'a': {u'd': {u'd': {'#': '#'}}, 
        u't': {'#': '#'}, 
        u'n': {'#': '#',
               u'd': {'#': '#'}}}, 
}

obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
print(obj.prefix_tree)
print(obj.search('a'))
print(obj.search('.at'))
obj.addWord('bat')
print(obj.search('.at'))
print(obj.search('an.'))

{'a': {'d': {'d': {'#': '#'}}, 't': {'#': '#'}, 'n': {'#': '#','d': {'#': '#'}}}}
{'a': {'t': {'#': '#'}, 'n': {'d': {'#': '#'}, '#': '#'}, 'd': {'d': {'#': '#'}}}}
{'a': {'t': {'#': '#'}, 'n': {'d': {'#': '#'}, '#': '#'}, 'd': {'d': {'#': '#'}}}}