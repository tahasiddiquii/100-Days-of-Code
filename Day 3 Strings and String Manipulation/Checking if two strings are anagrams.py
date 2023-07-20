def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase to make the comparison case-insensitive
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of the two strings are equal
    if len(str1) != len(str2):
        return False

    # Convert both strings to lists and sort them
    sorted_str1 = sorted(list(str1))
    sorted_str2 = sorted(list(str2))

    # Compare the sorted lists
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False


string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
