from stats import word_count
from stats import character_count
from stats import sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # First, check if the command line arguments are correct
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # If we get here, we have the right number of arguments
    path = sys.argv[1]  # Use the path from command line
    
    text = get_book_text(path)
    num_words = word_count(text)
    char_dictionary = character_count(text)
    sorted_characters = sorted_dict(char_dictionary)
    
    print(f"Found {num_words} total words.")
    for entry in sorted_characters:
        if entry["character"].isalpha():  # Only consider alphabetical characters
            print(f"{entry['character']}: {entry['count']}")
            

main()
