def word_count(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words
    
def character_count(book_text):
    book_text = book_text.lower()  # Convert the entire string to lowercase first
    characters = list(book_text)  
    character_dictionary = {}
    for ch in characters:
        if ch not in character_dictionary:
            character_dictionary[ch] = 1  # Add the character with a count of 1
        else:
            character_dictionary[ch] += 1 
    return character_dictionary

    
def sorted_dict(character_dictionary):
    characters_list = []
    for ch, count in character_dictionary.items():
        characters_list.append({"character": ch, "count": count})
    # Now, sort the list by the "count" key in descending order
    sorted_list = sorted(characters_list, key=lambda entry: entry["count"], reverse=True)
    return sorted_list