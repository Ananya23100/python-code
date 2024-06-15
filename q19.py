import string

str1=input("enter a string")
clean_str1=" "
for char in str1:
    if char not in string.punctuation:
        clean_str1=clean_str1+char
print("the string with removed punctuation is :",clean_str1)