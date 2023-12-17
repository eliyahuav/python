def sort_anagrams(list_of_strings):

    sorted_words = []
    
    for word in list_of_strings:

        sorted_word = sorted(word)
        found = False
        
        for pair in sorted_words:
            if pair[0] == sorted_word:  # If a matching sorted word is found
                pair[1].append(word)  # Append the word to its respective list
                found = True
                break
        
        # If the sorted word is not found in the sorted_words list, add it along with the word
        if not found:
            sorted_words.append([sorted_word, [word]])
    
    # Extract the words from the sorted_words list and return as a list of lists
    result = [pair[1] for pair in sorted_words]
    
    return result
    

# ----------main----------------------------------------
def main():

    list_of_words = ['deltas', 'retainers', 'desalt',
                     'pants', 'slated', 'generating',
                     'ternaries', 'smelters', 'termless',
                     'salted', 'staled', 'greatening',
                     'lasted', 'resmelts']
    
    print(sort_anagrams(list_of_words))

if __name__ == "__main__":
    main()