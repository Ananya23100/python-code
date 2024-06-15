str1=input("Enter the string")
pref=input("Enter the prefix of the string you want to check")
suff=input("Enter the suffix of the string you want to check")
if str1.startswith(pref) and str1.endswith(suff):
    print("Yes it starts with ",pref,"and ends with ",suff)
elif str1.startswith(pref):
    print("Yes,its starts with ",pref)
elif str1.endswith(suff):
    print("Yes,its ends with ", suff)
else:
    print("The input is neither prefix or suffix of the input string")