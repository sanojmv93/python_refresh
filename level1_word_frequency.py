import collections

if __name__ == "__main__":
    i = input("Enter the sentence: ")
    mv = i.split()
    m = [x.lower() for x in mv]
    q = collections.Counter(m)
    print("The word frequencies are as follows: ", dict(q))