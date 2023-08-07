def find_longest_words(text):
    words = text.split()
    longest_words = []

    max_length = 0
    for word in words:
        word_length = len(word)
        if word_length > max_length:
            longest_words = [word]
            max_length = word_length
        elif word_length == max_length:
            longest_words.append(word)

    return longest_words

if __name__ == "__main__":
    input_text = input("Enter a sentence or paragraph: ")
    longest_words = find_longest_words(input_text)

    if longest_words:
        print(f"Longest word(s): {', '.join(longest_words)}")
    else:
        print("No words found.")
