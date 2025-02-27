def check_palindrome(string):
    string = ''.join(s.split()).lower()

    return string == string[::-1]

s = input("Enter your string: ")

if check_palindrome(s):
    print("Yes, string is palindrome!")
else:
    print("No, string is not palindrome(")