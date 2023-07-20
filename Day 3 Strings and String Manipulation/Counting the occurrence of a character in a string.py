def count_char_occurrence(input_string, char):
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    return count


input_str = "Hello, how are you?"
character_to_count = "o"
result = count_char_occurrence(input_str, character_to_count)
print(
    f"The character '{character_to_count}' occurs {result} times in the string.")
