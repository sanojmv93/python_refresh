import collections

def isomorphic(x, y):
    a = dict(collections.Counter(x))
    b = dict(collections.Counter(y))
    if list(a.values()) == list(b.values()):
        return True
    else:
        return False
    

if __name__ == "__main__":
    a = input("Enter string 1:")
    b = input("Enter string 2:")
    x = isomorphic(list(a), list(b))
    if x:
        print("The strings are isomorphic...")
    else:
        print("The strings are not isomorphic...")
