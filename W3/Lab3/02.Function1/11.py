def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Убираем пробелы и приводим к нижнему регистру
    return s == s[::-1]

#Example
print(is_palindrome("madam")) 
print(is_palindrome("hello"))  
print(is_palindrome("A Santa at NASA"))  
