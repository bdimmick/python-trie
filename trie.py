

class Trie:

    def __init__(self):
        self.path = {}
        self.value = None

    def __setitem__(self, key, value):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            node = Trie()
            self.path[head] = node

        if len(key) > 1:
            remains = key[1:]
            node.__setitem__(remains, value)
        else:
            node.value = value

    def __delitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
            if len(key) > 1:
                remains = key[1:]
                node.__delitem__(remains)
            else:
                node.value = None
            if len(node) == 0:
                del self.path[head]

    def __getitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
        else:
            return None
        if len(key) > 1:
            remains = key[1:]
            return node.__getitem__(remains)
        else:
            return node.value

    def __contains__(self, key):
        return not self.__getitem__(key) == None

    def __len__(self):
        n = (self.value and 1) or 0
        for k in self.path.iterkeys():
            n = n + len(self.path[k])
        return n

    def nodeCount(self):
        n = 0
        for k in self.path.iterkeys():
            n = n + 1 + self.path[k].nodeCount()
        return n

    def keys(self, prefix=[]):
        result = []
        if self.value != None:
            isStr = True
            val = ""
            for k in prefix:
                if type(k) != str or len(k) > 2:
                    isStr = False
                    break
                else:
                    val += k
            if isStr:
                result.append(val)
            else:
                result.append(prefix)
        for k in self.path.iterkeys():
            next = []
            next.extend(prefix)
            next.append(k)
            result.extend(self.path[k].keys(next))
        return result

    def __iter__(self):
        for k in self.keys():
            yield k
        raise StopIteration

    def __add__(self, other):
        result = Trie()
        result += self
        result += other
        return result

    def __sub__(self, other):
        result = Trie()
        result += self
        result -= other
        return result

    def __iadd__(self, other):
        for k in other:
            self[k] = other[k]
        return self

    def __isub__(self, other):
        for k in other:
            del self[k]
        return self
