# String helper functions
# Assignment 5 - Parth Dadhaniya

def capitalize_words(text):
    # Capitalize the first letter of every word
    # python's title() method handles this easily
    return text.title()

def reverse_string(text):
    # Reverses the text using string slicing [::-1]
    # took me a minute to remember slicing syntax!
    return text[::-1]

def word_count(text):
    # Counts words by splitting on whitespace
    # print("DEBUG: split string is", text.split())
    words = text.split()
    return len(words)

if __name__ == "__main__":
    test_str = "learning python modules and packages"
    print("Test capitalize:", capitalize_words(test_str))
    print("Test reverse:", reverse_string(test_str))
    print("Test word count:", word_count(test_str))
