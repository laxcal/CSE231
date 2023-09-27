###########################################################
# Computer Project #9
# This program reads in a file of words and creates a dictionary of word 
#   completions, where each key is a tuple (i, l), where i is the index of a
#       letter in a word, and l is the letter at that index. The value associated
#           with each key is a set of words that have the same letter at the specified
#               index i. The program then prompts the user for a prefix and prints the 
#                   completions of that prefix, sorted in alphabetical order. The program 
#                       continues to prompt the user until the user enters the '#' character to quit.
###########################################################

'''
Main data structure is a dictionary
   word_dic[(i,ch)] = set of words with ch at index i
'''
import string

def open_file ( ):
    '''
    Asks the user for a file name and attempts to open the file with UTF-8 encoding.
    If the file s found, returs a file pointer. If te file is not found, an error
    message is printed and the user is asked to input another file name.
    Returns: pointer: file pointer if file is found
    '''
    while True:
        # Ask user for file name input
        f_n = input("\nInput a file name: ")
        try:
            # Attempt to open file with UTF-8 encoding
            pointer = open(f_n , encoding='UTF-8')
            return pointer
        except FileNotFoundError:
            # Print error message if file is not found
            print("\n[Error]: no such file")

def read_file(fp):
    '''This function takes a file pointer as anargument and reads
    the fileline by line, extracting unique words from each line.
    The function removes any leading or railing punctuation marks from the words,
    and discards any words that are not alphabetic or hae length of 1.
    Finally, the function returns a set of unique words from the entire file.'''
    # Create an empty set to store unique words
    file_words = set( )
    # Iterate over each line in the file
    for l_ing in fp:
        # Split the line into words
        for text in l_ing.split( ):
            # Remove leading and trailing punctuation from the word
            text = text.strip(string.punctuation)
            # Check if the word contains only alphabetic characters and has length greater than 1
            if text.isalpha( ) and len(text) > 1:
                # Add the lowercase word to the set of unique words
                file_words.add(text.lower( ) )
    # Return the set of unique words
    return file_words

def fill_completions(words):
    """ Given a list of words, returns a dictionary where each key is a tuple (i, l), 
    wher i is the index of a letter in a wor, and l is the letter at that index. The value 
    associated with each keyis a set of ords that have the same letter at the specified index i. 
    Args: words (list): A list of stings representing words.
    Returns: dict: A dictionary where each key is a tuple (i, l), where i is the index of a
    letter in a word, and l is the letter at that index. The value associated 
    with each key is a set of wrds that have the same letter at the specified index i. 
    """
    # create an empty dictionary to store the results
    final = { }
    # loop over each word in the list of words
    for text_2 in words:
        # loop over each letter and its index in the word
        for I_ing , L_ing in enumerate(text_2):
            # create a key tuple with the current index and letter
            letters_1 = (I_ing , L_ing)
            # if the key doesn't exist in the dictionary, create a new set as the value
            # and add the current word to the set
            # otherwise, add the current word to the set associated with the existing key
            if letters_1 not in final:
                final[letters_1] = set( )
            final[letters_1].add(text_2)

    # return the final dictionary
    return final

def find_completions(prefix , word_dic):
    """ Given a prefix and a dictionary of words, returns a set of all words that
    startwith he given prefix.
    Args: prefix (str): The prefix to search for in the dictionary.
    word_dic (dict): A dictionary that maps each (inex, letter) tuple to a set
    of words that start with that prefix.
    Returns: A set of all words inthe dictionary that start with the given prefix.
    If the prefix is empty or not found in the dictionary, anempty set is returned.
    """
     # Initialize a variable to keep track of the intersection of word sets
    # that match each character in the prefix
    totals = None
    # If the prefix is empty, return an empty set
    if not prefix:
        return set( )
    # Iterate over each character in the prefix
    for I_ing_2 , L_ing_2 in enumerate(prefix):
        # Create a key to look up in the word_dic dictionary
        letters_2 = (I_ing_2 , L_ing_2)
        # If the key exists in the word_dic dictionary, find the intersection
        # of the corresponding set of words with the current set of totals
        if letters_2 in word_dic:
            if totals is None:
                totals = word_dic [letters_2]
            else:
                totals = totals.intersection(word_dic [letters_2] )
        else:
            # If the key does not exist in the word_dic dictionary, return an empty set
            return set( )
    # Return the final set of words that match the prefix
    return totals

def main():
    ''' Main funtion that interacts with the user and calls other functions to
    read a file of words, create a dictionary of wrd completions, and find
    completions of a given prefix.
    '''
    point = open_file( )  # Calls function to open a file and returns a file object
    file_words = read_file(point)  # Calls function to read the file and returns a list of words
    final = fill_completions(file_words)  # Calls function to create a dictionary of word completions
    str_k = [ ]  # A list to hold string representations of dictionary keys
    for letters_3 in final:
        ks = str(letters_3)
        str_k.append(ks)  # Adds the string representation of each key to the str_k list
    sorted_keys = sorted(str_k)  # Sorts the list of string keys in alphabetical order
    while True:
        prefix = input("\nEnter a prefix (# to quit): ")
        if prefix == "#":
            print("\nBye")
            break
        final_2 = find_completions(prefix , final)  # Calls function to find completions of a given prefix
        if final_2:
            print("\nThe words that completes {} are: {}".format(prefix , ', ' .join(sorted(final_2) ) ) )
            # If there are completions, prints them in alphabetical order
        else:
            print("\nThere are no completions.")
            # If there are no completions, prints a message saying so
if __name__ == '__main__':
    main( )