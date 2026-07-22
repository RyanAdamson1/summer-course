# Error 1
text = ("hello world")
text.join("!")  # append() is for lists, not strings
print(text)

# Error 2
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Extra 'd'
print(numbers)

# Error 3
result = print("Hello")  # print() returns None
length = result.upper(result)  # Can't call .upper() on None