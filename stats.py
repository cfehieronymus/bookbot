def countWords(wordList):
    numberOfWords = len(wordList)
    return numberOfWords

def getWordList(text):
    wordList = text.split()
    return wordList

def countCharacters(text):
    characterDict = {}
    
    for character in text:
        lowercase_character = character.lower()
        if lowercase_character in characterDict:
            characterDict[lowercase_character] += 1
        else:
            characterDict[lowercase_character] = 1

    return characterDict

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(char_dict):
    chars_list=[]

    for char, count in char_dict.items():
        
        chars_list.append({"char": char, "num": count})

    chars_list.sort(key=sort_on, reverse=True)
    
    return chars_list
