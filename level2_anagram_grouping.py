from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    inp = input("Enter the list of strings: ").split()
    u = group_anagrams(inp)
    print(u)
    