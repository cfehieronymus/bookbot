import sys
from stats import countWords, getWordList, countCharacters, chars_dict_to_sorted_list

def getBookText(path):
    with open(path) as f:
        fileContents = f.read()
        return fileContents
    


def main():

    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1] # Get the path from command line arguments
    text = getBookText(path)
    wordList = getWordList(text)
    wordCount = countWords(wordList)
    characterDict = countCharacters(text)
    # Get sorted list of character counts
    sorted_chars = chars_dict_to_sorted_list(characterDict)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")

    # Print each character and its count
    for char_data in sorted_chars:
        if char_data["char"].isalpha(): # Only print alphabetical characters
            print(f"{char_data['char']}: {char_data['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

    