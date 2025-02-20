import re

# 1. Match a string that has an 'a' followed by zero or more 'b''s
def match_a_followed_by_b(string):
    return bool(re.fullmatch(r'ab*', string))

# 2. Match a string that has an 'a' followed by two to three 'b'
def match_a_followed_by_2_to_3_b(string):
    return bool(re.fullmatch(r'ab{2,3}', string))

# 3. Find sequences of lowercase letters joined with an underscore
def find_lowercase_underscore(string):
    return re.findall(r'\b[a-z]+_[a-z]+\b', string)

# 4. Find sequences of one uppercase letter followed by lowercase letters
def find_uppercase_followed_by_lowercase(string):
    return re.findall(r'[A-Z][a-z]+', string)

# 5. Match a string that has an 'a' followed by anything, ending in 'b'
def match_a_anything_b(string):
    return bool(re.fullmatch(r'a.*b', string))

# 6. Replace all occurrences of space, comma, or dot with a colon
def replace_with_colon(string):
    return re.sub(r'[ ,.]', ':', string)

# 7. Convert snake case string to camel case string
def snake_to_camel(string):
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(string.split('_')))

# 8. Split a string at uppercase letters
def split_at_uppercase(string):
    return re.split(r'(?=[A-Z])', string)

# 9. Insert spaces between words starting with capital letters
def insert_spaces_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

# 10. Convert a given camel case string to snake case
def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

# Testing the functions
test_string = "HelloWorld"
print(match_a_followed_by_b("ab"))  # True
print(match_a_followed_by_2_to_3_b("abb"))  # True
print(find_lowercase_underscore("hello_world test_example"))
print(find_uppercase_followed_by_lowercase("HelloWorld TestCase"))
print(match_a_anything_b("axxxb"))  # True
print(replace_with_colon("Hello, world. This is a test."))
print(snake_to_camel("hello_world_example"))
print(split_at_uppercase("SplitAtUppercase"))
print(insert_spaces_capitals("InsertSpacesBetweenWords"))
print(camel_to_snake("ConvertThisToSnakeCase"))
