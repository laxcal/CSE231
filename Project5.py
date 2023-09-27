###########################################################
#  Computer Project #5
# Reads files with anime records and addresses prompts
#   Tells user anime with highest score
#       Titles with highest number of episeodes
#           Titles with the lowest scores
#   Reads files to recieve max, min, and average values
#       Displays multiple anime if happen to have same score or episodes
#           User can exit the program
###########################################################

 
'''This code implements a command line program for processing and 
analyzing data on anime from Anime-Planet.com. The program provides 
two options. 1) getting statistics on the highest/lowest anime scores. 
highest episode count, and average score; and 2) searching for anime 
titles by name. The program reads data from a file and uses several 
functions to process and analyze the data. The program will continue 
to run until the user chooses to exit.'''

def open_file():
    '''
    Prompts user to enter filename and opens file if found.
    Returns: file_processing: opened file object
    '''
    # This is an infinite loop that keeps asking the user for a filename
    while True:
        # Ask the user to enter a filename.
        filename = input("\nEnter filename: ")
        try:
            # Try to open the file with the filename given by the user, using the utf-8 encoding.
            # If the file is successfully opened, return the file object for further processing.
            file_processing = open(filename, "r", encoding="utf-8")
            return file_processing
        except FileNotFoundError:
            # If the file is not found, print an error message and continue with the loop.
            print(f"\nFile not found!")
            
def find_max(num, name, max_num, max_name):
    '''The function find_max takes four arguments: num, name, max_num, 
       and max_name, and returns a tuple containing the maximum value 
       and its corresponding name. If the num parameter is
       greater than the max_num parameter, both the maximum value and 
       name are updated. If num is equal to max_num, the name is
       appended to max_name. If num is less than max_num, 
       the function returns the original max_num and max_name values.'''

    if num > max_num:
        # if current num is greater than current max_num, update both
        return num, "\n\t{}".format(name)
    elif num == max_num:
        # if current num is equal to current max_num, append name to max_name
        return max_num, "{}\n\t{}".format(max_name, name)
    else:
        # otherwise, keep max_num and max_name as they are
        return max_num, max_name

    
def find_min(num, name, min_num, min_name):
    '''Python function to find the minimum number and corresponding name in a dataset, 
    using four input parameters: 'num', 'name', 'min_num', and 'min_name'. The function returns the 
    minimum number and name. This function is useful for finding the minimum value in 
    a large dataset quickly and efficiently, without having to sort 
    the entire dataset or iterate through all the elements.'''
    if num < min_num:
        return num, "\n\t{}".format(name)
    elif num == min_num:
        return min_num, "{}\n\t{}".format(min_name, name)
    else:
        return min_num, min_name

def read_file(data_fp):
    '''This code reads data from a file and calculates some statistics,
     such as maximum and minimum scores, maximum number of episodes, 
     and average score. It uses helper functions to find the maximum 
     and minimum values. The function returns these calculated statistics.'''
    # Initialize variables to hold various statistics
    MaxEpName = ''     # title of the show with the maximum number of episodes
    MinScoreName = ''       # title of the show with the minimum score
    MinScore = float('inf')  # initialize to infinity so that the first score will always be less
    SummartScore = 0.0           # initialize to 0 to calculate the sum of all scores
    MaxEp = float('-inf')  # initialize to negative infinity so that the first episode count will always be greater 
    MaxScoreName = ''       # title of the show with the maximum score
    Counts = 0           # keep track of the number of scores seen
    MaxScore = float('-inf') # initialize to negative infinity so that the first score will always be greater

    # Iterate over each line in the file
    for line in data_fp:
        # Extract relevant information from line
        title = line[0:100].strip()     # extract the title from the first 100 characters 
        score_str = line[100:105].strip()   # extract the score from characters 101-105 of the line
        episodes_str = line[105:110].strip()   # extract the number of episodes from characters 106-110 of the line
                # Calculate statistics for episode counts
        if episodes_str != "N/A":   # only process episode counts that are not "N/A"
            episodes = float(episodes_str)   # convert the episode count to a floating-point number
            MaxEp, MaxEpName = find_max(episodes, title, MaxEp, MaxEpName)   # update the maximum episode count and corresponding show title using the find_max() function
        # Calculate statistics for scores
        if score_str != "N/A":   # only process scores that are not "N/A"
            score = float(score_str)   # convert the score to a floating-point number
            SummartScore += score    # add the score to the running sum of all scores
            Counts += 1      # increment the number of scores seen
            MinScore, MinScoreName = find_min(score, title, MinScore, MinScoreName)   # update the minimum score and corresponding show title using the find_min() function
            MaxScore, MaxScoreName = find_max(score, title, MaxScore, MaxScoreName)   # update the maximum score and corresponding show title using the find_max() function

    # Calculate average score
    AverageScore = round(SummartScore / Counts, 2) if Counts > 0 else 0.0   # calculate the average score by dividing the sum of all scores by the number of scores seen

    # Return statistics
    return MaxScore, MaxScoreName, MaxEp, MaxEpName, MinScore, MinScoreName, AverageScore   
    # return a tuple containing the maximum score and corresponding show title, the maximum episode count and corresponding show title, the minimum score and corresponding show title, and the average score

    
        
def search_anime(data_fp, anime_name):
    '''
    Searches for anime titles that contain a given name.
    data_fp (file object): A file object representing the data file to search.
    anime_name (str): The name to search for in the anime titles.
    count (int): The number of anime titles found.
    releasestring (str): A formatted string containing the anime titles found.
    '''
    # Initialize the count and output string variables
    releasestring = ""
    count = 0
    
    # Iterate over each line in the data file.
    for line in data_fp:
        # Extract the title and release season information 
        title = line[0:100]  # The title is the first 100 characters 
        release_season = line[110:122]  # The release season is characters 110-122 

        # Check if the anime name is present in the title, and add it to the output string if it is.
        if anime_name in title:
            count += 1  # Increment the count variable
            # Format the title and release season information and add it to the output string
            releasestring += "\n\t{}{}".format(title, release_season)

    # Return the count and output string variables
    return count, releasestring


def main():
    '''This program's main function is a command-line interface that offers two options: 1)
    Get max/min statistics from an anime data file, and 2) Search for anime titles
    containing a given name. The program reads data from a file using the helper 
    function "read_file", searches for anime titles using the helper function "search_anime", 
    and prints the results to the console. The program includes a banner with the program name 
    and data year, and a menu with options for the user to choose from. The program runs in a
    loop until the user chooses to stop it. This program 
    can be imported into other code for testing purposes.'''
    # Define the menu options.
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    # Print a banner with the program name and data year.
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    print(BANNER)
    while True:
        # Ask the user to choose an option from the menu.
        option = input(MENU)

        # Option 1: Get max/min statistics from the data file.
        if option == "1":
            FileProcessing = open_file()
            MaxScore, MaxScoreName, MaxEp, MaxEpName, MinScore, MinScoreName, AverageScore = read_file(FileProcessing)
            print(f"\n\nAnime with the highest score of {MaxScore}:\n{MaxScoreName}")
            print(f"\n\nAnime with the highest episode count of {int(MaxEp):,}:\n{MaxEpName}")
            print(f"\n\nAnime with the lowest score of {MinScore:.2f}:\n{MinScoreName}")
            print(f"\n\nAverage score for animes in file is {AverageScore}")
            FileProcessing.close()

        # Option 2: Search for anime titles containing a given name.
        elif option == "2":
            FileProcessing = open_file()
            anime_name = input("\nEnter anime name: ")
            count, releasestring = search_anime(FileProcessing, anime_name)
            if count == 0:
                print(f"\nNo anime with '{anime_name}' was found!")
            else:
                print(f"\nThere are {count} anime titles with '{anime_name}'")
                print(f'{releasestring}')
            FileProcessing.close()

        # Option 3: Stop the program.
        elif option == "3":
            print("\nThank you using this program!")
            break

        # Invalid option: Ask the user to try again.
        else:
            print("\nInvalid menu option!!! Please try again!")
# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()