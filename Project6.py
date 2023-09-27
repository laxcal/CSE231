###########################################################
#  Computer Project #6
# Defines constants for specific column indexes in a CSV file
# Defines a welcome menu and input prompts for the user
# Defines functions to read a CSV file and search for books based on criteria and keywords
# Defines a function to sort a list of tuples by author name
# Defines a function to recommend books based on criteria and keywords
# Defines a function to display a formatted table of book details
# Defines a main function to execute the program
# The program prompts the user to enter a filename, reads the CSV file, and displays a menu of options for the user to choose from.
# User ends program when chooses the option '4' 
###########################################################
import csv
from operator import itemgetter

TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "
TITLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}"
TABLE_FORMAT = "{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15d} {:<15d}"

def open_file():
    """Open a file and return its file pointer.
    Asks the user to enter a file name and tries to open the file with the
    given name. If the file does not exist or cannot be opened, an error
    message is printed and the user is prompted to enter a file name again.
    Returns: The file pointer of the opened file.
    Exceptions: This function does not raise any exceptions."""
    # Use a while loop to keep asking for a file name until a valid file
    # is opened or the user terminates the program.
    while True:
        try:
            filename = input("Enter file name: ")
            # Use the built-in open() function to open the file in read mode
            # with the specified encoding.
            fp = open(filename, "r", encoding="utf-8")
            # If the file is opened successfully, return its file pointer.
            return fp
        except (IOError, FileNotFoundError):
            # If there is an error opening the file, print an error message
            # and continue the loop to prompt the user for another file name.
            print("\nError opening file. Please try again.")
def read_file(fp):
    """Read a CSV file containing book data and return a list of tuples.
    Reads the CSV file line by line and extracts relevant data for each book,
    including ISBN, title, authors, categories, description, year of publication,
    average rating, number of pages, and number of ratings. Ignores any rows that
    cannot be parsed.
    Args: fp: A file pointer to an open CSV file.
    Returns: A list of tuples, where each tuple represents a book and contains the
    following elements in order: ISBN-13, title, authors (comma-separated),
    categories (list of strings), description, year of publication (integer),
    average rating (float), number of pages (integer), and number of ratings (integer).
    Exceptions: This function does not raise any exceptions."""
    # Skip the first line of the file, which contains column headers.
    next(fp)
    # Initialize an empty list to store the book data.
    books = []
    # Use the built-in csv module to read the file in CSV format.
    csv_reader = csv.reader(fp)
    # Iterate over each row in the CSV file.
    for row in csv_reader:
        try:
            # Extract the relevant columns from the row and strip any whitespace.
            isbn13, isbn10, title, subtitle, authors, categories, thumbnail, description, \
            published_year, average_rating, num_pages, ratings_count = [stuff.strip() for stuff in row]
            # Split the categories string into a list of lowercase strings.
            categories = [cat.lower() for cat in categories.split(",")]
            # Convert the year, rating, pages, and rating_count columns to their respective data types.
            year = (published_year)
            rating = float(average_rating)
            pages = int(num_pages)
            rating_count = int(ratings_count)
            # Create a tuple representing the book and append it to the list of books.
            book = (isbn13, title, authors, categories, description, year, rating, pages, rating_count)
            books.append(book)
        except:
            # If there is an error parsing the row, skip it and continue to the next row.
            continue
    # Return the list of books.
    return books


def get_books_by_criterion(list_of_tuples, criterion, value):
    """Return a list of books matching a given search criterion and value.
    Searches a list of book tuples for books that match a given search criterion and value.
    The search criterion can be one of "title", "category", "year", "rating", or "pages".
    For each book that matches the search criterion and value, a tuple representing the book
    is appended to a list of results. If no books match the search criterion and value, an
    empty list is returned.
    Args:
    list_of_tuples: A list of book tuples, where each tuple represents a book and
    ontains the following elements in order: ISBN-13, title, authors (comma-separated),
    categories (list of strings), description, year of publication (integer),
    average rating (float), number of pages (integer), and number of ratings (integer).
    criterion: A string representing the search criterion, which can be one of "title",
    "category", "year", "rating", or "pages".
    value: A string representing the search value.
    Returns:
    A list of tuples, where each tuple represents a book that matches the search criterion
    and value, and contains the relevant data in a specific order. If no books match the
    search criterion and value, an empty list is returned. If the search criterion is "title"
    and exactly one book matches the search criterion and value, a single tuple is returned
    instead of a list.
    Raises:
        This function does not raise any exceptions."""
    # Initialize an empty list to store the results.
    result = []
    # Iterate over each book tuple in the list of tuples.
    for book in list_of_tuples:
        # Check the search criterion and value against the corresponding elements of the book tuple.
        if criterion == TITLE and value.lower() == book[TITLE].lower():
            # If the search criterion is "title" and exactly one book matches the search criterion and value,
            # return a single tuple instead of a list.
            return book
        elif criterion == CATEGORY and value.lower() in book[CATEGORY]:
            result.append(book)
            # If the search criterion is "category" append the specific criterion number and book list to list.
        elif criterion == YEAR and value == book[YEAR]:
            result.append(book)
            # If the search criterion is "year" append the specific criterion number and book list to list.
        elif criterion == RATING and float(value) <= book[RATING]:
            result.append(book)
            # If the search criterion is "rating" append the specific criterion number and book list to list.
        elif criterion == PAGES and (int(value) - 50 <= book[PAGES] <= int(value) + 50):
            result.append(book)
    # If no books match the search criterion and value, return an empty list.
    # Otherwise, return the list of results.
    return result
def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    """ Filters a list of books by category, rating, and page number.
    Parameters:
    list_of_tuples (list): A list of tuples representing books.
    category (str): The category to filter by.
    rating (float): The minimum rating to filter by.
    page_number (int): The target number of pages to filter by.
    Returns:
    list: A list of books matching the criteria."""
    # Filter books by category
    category_filter = get_books_by_criterion(list_of_tuples, criterion=CATEGORY, value=category)
    # Filter books by rating
    rating_filter = get_books_by_criterion(category_filter, criterion=RATING, value=rating)
    # Filter books by page number
    page_filter = get_books_by_criterion(rating_filter, criterion=PAGES, value=page_number)
    # Return the final list of books
    return page_filter

def get_books_by_keyword(list_of_tuples, keywords):
    """ Filters a list of books by keywords in the book description.
    Parameters:
    list_of_tuples (list): A list of tuples representing books.
    keywords (list): A list of keywords to search for.
    Returns:
    list: A list of books containing at least one of the keywords in the book description. """
    # Initialize an empty list to store the matching books
    end = []
    # Loop through each book in the list of tuples
    for book in list_of_tuples:
        # Loop through each keyword in the list of keywords
        for keyword in keywords:
            # Check if the keyword is in the book description (case-insensitive)
            if keyword.lower() in book[4].lower() and book not in end:
                # If the keyword is in the book description and the book has not been added to the result list,
                # add the book to the result list and break out of the keyword loop to avoid adding duplicates
                end.append(book)
                break
    # Return the final list of matching books
    return end

def sort_authors(list_of_tuples, a_z=True):
    """ Sorts a list of books by author name in ascending or descending order.
    Parameters:
    list_of_tuples (list): A list of tuples representing books.
    a_z (bool, optional): If True, sorts in ascending order (A-Z); if False, sorts in descending order (Z-A).
    Defaults to True.
    Returns:
    list: A sorted list of tuples representing books, sorted by author name."""
    # Make a copy of the list to avoid modifying the original list
    sorted_author = list_of_tuples[:]
    # Sort the list by author name using the itemgetter function
    sorted_author.sort(key=itemgetter(2))
    # Reverse the list if a_z is False (descending order)
    if not a_z:
        sorted_author.reverse()
    # Return the final sorted list
    return sorted_author

def recommend_books(list_of_tuples, keywords, category, rating, page_number, a_z):
    """ Recommends books that match the given criteria, sorted by author name.
    Parameters:
    list_of_tuples (list): A list of tuples representing books.
    keywords (list): A list of keywords to search for in the book descriptions.
    category (str): The category to search for in the book categories.
    rating (float): The minimum rating a book must have to be recommended.
    page_number (int): The desired number of pages for the recommended books.
    a_z (bool, optional): If True, sorts the recommended books in ascending order (A-Z) by author name;
    if False, sorts in descending order (Z-A). Defaults to True.
    Returns:
    list: A sorted list of tuples representing recommended books that match the given criteria."""
    final = []
    # Iterate over each book in the list of tuples
    for book in list_of_tuples:
        # Check if the book matches the category, rating, and page number criteria
        if category in book[CATEGORY] and rating <= book[RATING] and (int(page_number) - book[PAGES]) ** 2 <= 2500:
            # Iterate over each keyword in the list of keywords
            for keyword in keywords:
                # Check if the keyword appears in the book description and the book hasn't already been added to the result list
                book_title = book[4].lower()
                if keyword.lower() in book_title and book not in final:
                    final.append(book)
                    break
    sorted_list = sort_authors(final, a_z)
    return sorted_list

def display_books(list_of_tuples):
    """ Displays a table of books with their relevant information.
    Parameters:
    list_of_tuples (list): A list of tuples representing books.
    Returns:
    None """
    if len(list_of_tuples) == 0:
        print("Nothing to print.")
    else:
        # Print the header row of the table
        print(TITLE_FORMAT.format('ISBN-13', 'Title', 'Authors', 'Year', 'Rating', 'Number Pages', 'Number Ratings'))
      
    for book in list_of_tuples:
        # Skip books with long titles or author names to ensure the table fits on the screen
        title = book[TITLE]
        authors = book[2]
        if len(title) > 35 or len(authors) > 35:
            continue
        # Print a row of the table for the current book
        print(TABLE_FORMAT.format(book[0], title, authors, book[YEAR], book[RATING], book[PAGES], book[8]))

def get_option():
    """Asks the user to input an option from a menu and returns the chosen option.
    Returns: An integer representing the chosen option.
    The function uses a while loop to keep prompting the user for input until they provide a valid option.
    If the user inputs a number outside the range of valid options (1-4), an error message is printed.
    If the user inputs something that is not a number, another error message is printed. """
    while True:
        try:
            option = int(input(MENU)) 
            # Prompts the user to input a number corresponding to a menu option.
            if 1 <= option <= 4: 
                # Checks if the input number is within the range of valid options.
                return option
            else:
                print("\nInvalid option") 
                # Prints an error message if the input number is not valid.
        except ValueError:
            print("\nInvalid input") 
            # Prints an error message if the input is not a number.

def main():
    """ This function is the main entry point of a program that allows the user to search for and display information about a list of books.
    Usage: Run the function to start the program.
    Follow the prompts to enter search criteria and display information about the books.
    Enter option 4 to quit the program. """
    # Open the file for reading
    fp = open_file()
    # Read the contents of the file into a list of book dictionaries
    books = read_file(fp)
    # Close the file
    fp.close()
    # Keep ooping until the user chooses to exit
    while True:
        # Get the user's option
        option = get_option()
        # If the user wants to search for a book by title...
        if option == 1:
            # Get the title to search for from the user
            title = input("\nInput a book title: ")
            # Search for books that match the given title
            book = get_books_by_criterion(books, TITLE, title)
            # If at least one matching book was found...
            if book:
                # Print out the details of the first matching book
                print('\nBook Details:')
                display_books([book])
            else:
                # Otherwise, print an error message
                print("\nInvalid input")
        # If the user wants to search for a book by criteria...
        elif option == 2:
            # Keep looping until the user enters a valid criterion
            while True:
                # Get the criterion to search by from the user
                criterion = input(CRITERIA_INPUT)
                # If the user entered a valid criterion...
                if criterion.isdigit() and int(criterion) in [3, 5, 6, 7]:
                    # Convert the criterion to an integer and exit the loop
                    criterion = int(criterion)
                    break
                else:
                    # Otherwise, print an error message and continue the loop
                    print("\nInvalid input")
            # Get the value to search for from the user
            value = input("\nEnter value: ")
            # If the criterion is rating, validate the input as a float
            if criterion in [RATING]:
                try:
                    if criterion == RATING:
                        value = float(value)
                except:
                    # If the input is not valid, print an error message and prompt the user again
                    print("\nInvalid input")
                    value = input("\nEnter value: ")
                    #continue
            # If the criterion is pages, validate the input as an integer
            elif criterion in [PAGES]:
                try:
                    if criterion == PAGES:
                        value = int(value)
                except:
                    # If the input is not valid, print an error message and prompt the user again
                    print("\nInvalid input")
                    value = input("\nEnter value: ")
            # If the criterion is year, no need to validate the input as it is a string
            elif criterion in [YEAR]:
                try:
                    if criterion == YEAR:
                        value = value
                except:
                    # If the input is not valid, print an error message and continue the loop
                    print("\nInvalid input")
                    continue
            # If the criterion is category, validate the input as a string
            elif criterion in [CATEGORY]:
                try:
                    if criterion == CATEGORY:
                        value = str(value)
                except:
                    # If the input is not valid, print an error message and continue the loop
                    print("\nInvalid input")
                    continue
            # Search for books that match the given criterion and value
            book = get_books_by_criterion(books, criterion, value)
            # Sort the matching books by author name in ascending order
            book = sort_authors(book, True)
            # Print out the details of the first 30 matching books
            print('\nBook Details:')
            display_books(book[:30])
        elif option == 3:
            # Get the desired category, rating, and page number from the user
            category = input("\nEnter the desired category: ")
            rating = input("\nEnter the desired rating: ")
            # Validate the input rating as a float
            try:
                rating = float(rating)
            except:
                # If the input is not valid, print an error message and continue the loop
                print("\nInvalid input")
                continue
            # Get the desired page number from the user
            page_num = input("\nEnter the desired page number: ")
            # Validate the input page number as an integer
            try:
                if page_num == int:
                    page_num = int(page_num)
            except:
                # If the input is not valid, print an error message and continue the loop
                print("\nInvalid input")
                continue
            # Ask the user if they want to sort the books in A-Z or Z-A order
            a_z = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ") 
            # Convert the user input to a boolean for sorting in ascending or descending order
            if a_z == "1":
                a_z = True
            elif a_z == "2":
                a_z = False
            else:
                a_z = False
            # Get keywords to search for from the user
            keywords = input("\nEnter keywords (space separated): ").split()
            # Recommend books based on the given criteria and keywords
            print('\nBook Details:')
            book = recommend_books(books, keywords, category, rating, page_num, a_z)
            display_books(book)
        # If the user wants to exit the program...
        elif option == 4:
            # Break out of the while loop and exit the program
            break
        # If the user entered an invalid option...
        else:
            # Print an error message and continue the loop
            print("\nInvalid input")
# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()