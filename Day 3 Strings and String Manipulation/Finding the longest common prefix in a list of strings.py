def longest_common_prefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the list
    shortest_str = min(strs, key=len)

    for i, char in enumerate(shortest_str):
        # Check if the character at the current position matches in all strings
        if all(string[i] == char for string in strs):
            continue
        else:
            return shortest_str[:i]

    return shortest_str  # If no mismatch is found, the shortest string is the common prefix


string_list = ["apple", "appetizer", "applause", "appliance"]

result = longest_common_prefix(string_list)
print("The longest common prefix is:", result)
