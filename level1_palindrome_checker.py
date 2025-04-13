def is_palindrom(s):
    m = s[::-1]
    u = False
    if s == m:
        u = True
        return u
    return u

if __name__ == "__main__":
    y = input("Enter the string: ")
    x = is_palindrom(y)
    if x:
        print("The string is paliindrome..")
    else:
        print("The string is not palindrome..")