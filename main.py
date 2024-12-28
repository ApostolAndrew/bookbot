def wordCount(book):
    return len(book.split())

def charCount(book):
    characters = {}
    for character in book:
        if character.lower() in characters:
            characters[character.lower()]+=1
        else:
            characters[character.lower()] = 1
    return characters

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    numWords = wordCount(file_contents)
    numChars = charCount(file_contents)
    numCharsSorted = dict(sorted(numChars.items(), key=lambda item: item[1], reverse=True))
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{numWords} words found in the document\n")

    for char in numCharsSorted:
        if char.isalpha():
            print(f"The '{char}' character was found {numCharsSorted[char]} times")
    print("--- End report ---")

main()