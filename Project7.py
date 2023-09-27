###############################################################
# Computer Project #7
# Algorithm:
# Prompt the user to enter city names.
#   Open files or each city and read data into a list of tuples.
#       Display a menu and prompt the user to choose an option.
#           Depending on the usr's choice, perform one of the following:
# Find the highest value for a specific column for all cities within a specified dae range.
#   Find the lowest value for a specific column for all cities within a specified date range.
#       Find the average value for a specific column for allcities within a specified date range.
#           Find the mode(s) for a specific column for all cities withn a specified date range.
# Display summary statistics for a specific column for a specific city within a spcified date range.
#      Find the hghest and lowest averages for each category across all data within a specified date range.
#           Quit the program.
# Repeat display menu until the user chooses to quit.
#   Display a closing message.
###############################################################

import csv   
from datetime import datetime   
from operator import itemgetter   

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    

MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
def open_files():
    '''
    Asks the user to enter a list of city names and opens a correspoding CSV file for each city.
    Returns a tuple of two lists, containing file names and file pointers respectively.
    Args: None
    Returns: A tuple of two lists:
    - files_from_data:a list of file names for the correspnding CSV files of the cities entered by the user.
    - fp_files: a list of file poiters for the corresponding CSV files of the cities entered by the user.
    Raises:
    FileNotFoundError: If a CSV file for a city entered by the user is not found, an error message is pinted and that file is not included in the returned lists.
    '''
    # Ask the user to input a list of city names
    dest_1 = input( "Enter cities names: " ).split( "," )
    # Create empty lists to hold file names and file pointers
    files_from_data = []
    fp_files =  []
    # Loop through the list of cities
    for destination in dest_1:
        # Generate a filename based on the city name and try to open the file
        filename_edited = f"{destination.strip()}.csv"
        try:
            file_pointer = open( filename_edited, "r" )
            # If the file is successfully opened, append the file pointer and filename to the respective lists
            fp_files.append(file_pointer )            
            files_from_data.append( filename_edited )
        except FileNotFoundError:
            # If the file is not found, print an error message
            print(f"\nError: File {filename_edited} is not found")
    # Return the list of file names and file pointers
    return  files_from_data , fp_files

def read_files(cities_fp):
    '''
    Reads CSV files for a list ofcities and parses the data into a list of tuples.
    Returns a list of data for all cities.
    Args:
    - cities_fp: a list of file pointers for the CSV files for the cities.
    Returns:
    - data: a list of lists, where each innr list contains tuples of daa for a city.
    Raises:None
    '''
    # Create an empty list to hold data for all cities
    data_in_files =  []
    # Loop through the file pointers for the CSV files for the cities
    for filep in cities_fp:
        # Create an empty list to hold data for the current city
        data2 =  []
        # Skip the first two lines of the CSV file
        next(filep)
        next(filep)
        # Loop through the remaining lines of the CSV file
        for line in filep:
            # Split the line into fields
            line_new_data = line.strip().split( ',' )
            # Check that the line has the correct number of fields
            if len(line_new_data) ==  7:
                # Convert numerical data to float
                # Create an empty list to hold the new data
                new_data =  []
                # Append the first value from the line to the list
                new_data.append(line_new_data[0] )
                # Loop through the remaining values in the line
                for i in range( 1, len(line_new_data) ):
                    # Get the value at the current index
                    value = line_new_data[i]
                    # Check if the value is an empty string
                    if value == '':
                        # If it is, append None to the new data list
                        new_data.append( None)
                    else:
                        # If it's not, convert it to a float and append it to the new data list
                        new_data.append(float( value ) )
                # Append the tuple to the list of data for the current city
                data2.append( tuple(new_data) )
        # Close the file handle
        filep.close()
        # Append the list of data for the current city to the list of data for all cities
        data_in_files.append(data2)
    # Return the data for all cities
    return  data_in_files

def get_data_in_range(master_list, start_str, end_str):
    '''
    Filters data from a list of lists of tuples based on a specified date range.
    Returns a new list of lists of tuples containing oly the filtered data.
    Args:
    - master_list: a list of lists of tuples containing data for multiple cities.
    - start_str: a string in the format "MM/DD/YYYY" representing the start date o the desired range.
    - end_str: a string in the frmat "MM/DD/YYY" representing the end date of the desired range.
    Returns:
    - data_new: a list of lists of tuples containing only the data that falls within th specified date range.
    Raises:None
    '''
    # Convert the start and end dates to datetime.date objects
    ending = datetime.strptime( end_str, "%m/%d/%Y").date()
    starting = datetime.strptime(start_str, "%m/%d/%Y").date()
    # Create an empty list to hold the filtered data
    data_new =  []
    # Iterate over each list in the master list
    for data_list in master_list:
        # Create a new list to hold the filtered data for the current list
        data_12 = []
        # Iterate over each tuple in the current list
        for data in data_list:
            # Convert the date in the tuple to a datetime.date object
            date_string = data [0]
            date_ =  datetime.strptime(date_string, "%m/%d/%Y").date()
            # Check if the date is within the specified range
            if starting <=  date_  <=  ending:
                # If so, append the tuple to the filtered data list for the current list
                data_12.append( data)
        # Append the filtered data list for the current list to the filtered data list
        data_new.append( data_12)
    # Return the filtered data list
    return  data_new

def get_min(col, data, cities):
    '''
    Returns a list of tuples containing the minimum value of the corresponding colun col for each city in cities.
    Args:
    - col: an integer representing the index of the column for which the minimum value is desired.
    - data: a list of lists o tuples containing data for multiple cities.
    - cities: a list of strings representing the names of the cities for which minimum values are desired.
    Returns:
    - new_results: a list of uples, where each tuple contains the name of a city and the minimu value of the specified column for that city.
    Raises:None
    '''
    # Helper function to get the minimum value of the column for a given city's data
    def get__value( city_data):
        """
        Helper function to get the minimum value of the column for a given city's data.
        Args:
        - city_data: a list or tuple representing the data for a given city.
        Returns: The minimum value of the specified column for the given city's data.
        """
        new =  []
        for w in city_data:
            # Check if the value in the column is not None
            if w [col] is not None:
                # If it's not None, append it to the list of values
                new.append( w[col] )
        # Return the minimum value from the list of values
        return min( new)
    # Create an empty list to hold the result
    new_results =  []
    # Iterate over each city and its corresponding data in the input lists
    for x in range( len( cities) ):
        city_name_1 = cities[x]
        city_data_1 = data[x]
        # Get the minimum value of the column for the current city's data
        city__value = get__value(city_data_1)
        # Append a tuple containing the city name and its corresponding minimum column value to the result list
        new_results.append( ( city_name_1, city__value) )
    # Return the result list
    return  new_results
        
def get_max(column, data, cities):
    '''
    Returns a list of tuples contaiing the maximum value of the corresponding column col for each city in cities.
    Args:
    - column: an integer representing the index of the column for which the maximum value is desired.
    - data: a list of list of tuples containing data for multiple cities.
    - cities: a list of strings representing the names of the cities for whch maximum values are desired.
    Returns:
    - result_macx: a list of tuples, where each tuple contains the name of a city and he maximum value of the specified column for that city.
    Raises:None
    '''
    # Helper function to get the maximum value of the column for a given city's data
    def col_values_1(city_12):
        """
        Helper function to get the maximum value of the column for a given city's data.
        Args:
        - city_data: a list or tuple representing the data for a given city.
        Returns: The maximum value of the specified column for the given city's data.
        """
        new_results_2 =  []
        for  t in city_12:
            # Check if the value in the column is not None
            if t  [column] is not None:
                # If it's not None, append it to the list of values
                new_results_2.append(t [column] )
        # Return the maximum value from the list of values
        return max( new_results_2)
    # Create an empty list to hold the result
    result_macx =  []
    # Iterate over each city and its corresponding data in the input lists
    for p in range( len(cities) ):
        city_121 = data [p]
        citynames = cities [p]
        # Get the maximum value of the column for the current city's data
        city_max_value =  col_values_1(city_121)
        # Append a tuple containing the city name and its corresponding maximum column value to the result list
        result_macx.append( ( citynames , city_max_value) )
    # Return the result list
    return  result_macx

def get_average(col, data, cities):
    '''Calculate the aerage value of a given column for each city in the dataset.
    Args:
    - col: An integer reprsenting the column to calculate the average for.
    - data: A lis of lists representing the data for eac city, where each inner list represents a row of data.
    - cities: A list of strings representing the names of the cities.
    Returns
    - A list of tuples containing each city's name and its average value for the specified column.
    '''
    # This is a helper function that takes in a city's data and returns the value of the given column
    def colum_val(city__dat):
        """
        Helper function to get the values of the given column for a given city's data.
        Args:
        - city_data: A list of lists representing the data for a given city, where each inner list represents a row of data.
        Returns: The average value of the specified column for the given city's data.
        """
        # Create an empty list to store the column values for this city
        col_data =  []
        # Iterate through each row of data for this city
        for h in city__dat:
            # If the value of the column for this row is not None, add it to the list of values for the column
            if h [col] is not None:
                col_data.append( h [col])
        # Check if there are any valid column values for this city
        if col_data:
            # Calculate the average of the column values for this city
            averag = round(sum( col_data) / len(col_data), 2)
            return averag
        else:
            # If there are no valid column values for this city, return None
            return  None
    # Create an empty list to store the tuples of city names and their average column values
    final =  []
    # Iterate through each city in the list of cities
    for q in range(len( cities) ):
        # Get the data for this city from the data list
        city__dat =  data [q]
        # Get the name of this city from the cities list
        cit = cities [q]
        # Call the helper function to calculate the average value of the column for this city
        averag = colum_val(city__dat)
        # Add a tuple of the city name and its average column value to the final list
        final.append( ( cit , averag) )
    # Return the list of tuples containing each city's name and its average value for the specified column
    return  final

def get_modes(col, data, cities):
    '''
    Returns the modes of a given column across multile datasets.
    Args:
        col (int): The index of the column to calculate modes for.
        data (list): A list of datasets, were each dataset is a list of rows.
        cities (list): A list of city names corresponding to each dataset.
    Returns:
        list: A lit of tuples, where each tuple contains the name of a city, the modes for the column in that cty, and the count of the most freqent mode.
    '''
    
    # TA help with the function on 4/1/2023

    list_of_modes =  []
    for i in range(len(data)):
        # Get the name and data for the current city
        name_of_city = cities [i]
        data_of_city = data [i]
        # Get the column values for the current city, ignoring None values
        collum_city = [item [col] for item in data_of_city if item [col] is not None]
        # If there are no values for the column, add an empty mode list with a count of 1
        if not collum_city:
            list_of_modes.append( (name_of_city , [] , 1) )
            continue
        collum_city.sort()
        streaks_in_data =  []
        # Initialize the first streak with the first value in the sorted column
        streak_ = collum_city [0]
        number_of_streak =  1
        for j in collum_city [1:]:
            # Check if the current value is close enough to the previous value to be part of the same streak
            if streak_  != 0:
                if abs( (streak_ -  j) / streak_)  <=  TOL:
                    number_of_streak  += 1
                # If the current value is not part of the same streak, add the previous streak to the list of streaks
                else:
                    if number_of_streak  >  1:
                        streaks_in_data.append( (number_of_streak , streak_) )
                    # Start a new streak with the current value
                    number_of_streak  =  1
                    streak_  =  j
            # Handle the special case where the previous value is 0 (to avoid dividing by zero)
            else:
                if number_of_streak  >  1:
                    streaks_in_data.append( (number_of_streak , streak_) )
                number_of_streak =  1
                streak_  =  j
        # Add the last streak to the list of streaks
        if number_of_streak  >   1:
            streaks_in_data.append( (number_of_streak , streak_) )
        # Find the streak with the highest count
        max_of_streak =  max(streaks_in_data, default = (1 , 0) )
        # Get the modes for the column by selecting the modes from streaks that have the same count as the max count
        # Initialize an empty list to store the mode values
        modes_data_ = []
        # Iterate through the streaks_in_data list, unpacking each tuple into 'streak' and 'mode'
        for s, m in streaks_in_data:
            # Check if the streak value is equal to the first element of the max_of_streak tuple
            if s == max_of_streak[0]:
                # If the condition is met, append the mode value to the modes_data_ list
                modes_data_.append(m)
        # Add the city name, modes, and max count to the modes_list
        max_count = max_of_streak [0]
        list_of_modes.append( (name_of_city , sorted(modes_data_) , max_count) )
    # Return the modes_list
    return list_of_modes

def high_low_averages(data, cities, categories):
    """
    Calculate the highst and lowest averages for a list of categories across a set of cities.
    Args:
        data List: A list of lists representing data for each city. 
            Each list contains rows of data forthe corresponding city, where each row is a list 
            of values for different categories.
        cities List: A lis of city names, where each city corresponds to a list of data 
            in the data parameter.
        categories (List[str): A list of category names for which to calculate the highest and 
            lowest averages.
    Returns:
        List: A list of results for each category in categories. Each result is a list containing a tuple for the lowest average 
            value an a tuple for the highest averagevalue. If a category is not found in the data, its corrsponding result is None.
    """
    # Create a list of lists to store the result
    # Initialize an empty list to store the results for each category
    final_res = []
    # Iterate over each category in the list of categories
    for cat in categories:
        # Initialize an empty list to store the city averages for the current category
        avg_cit = []
        # Check if the current category is in the COLUMNS list
        if cat not in COLUMNS:
            # If the category is not in the COLUMNS list, append None to the result list
            final_res.append( None)
            # Skip to the next iteration of the loop
            continue
        # Iterate over each city and calculate the average for the current category
        for s , cityis in enumerate(cities):
            # Get the index of the column for the current category
            collumn = COLUMNS.index(cat )
            # Create a list of values for the current category in the current city
            values =  []
            for row in data [s]:
                # If the value for the current row and column is not None, append it to the list of values
                if row [collumn] is not None:
                    values.append(row [collumn])
            # Calculate the average of the values for the current category in the current city
            if values:
                averagis = sum(values ) / len(values)
                # Add the city and its average for the current category to the list of city averages
                avg_cit.append( ( cityis, round(averagis, 2) ) )
        # If there are city averages for the current category, find the lowest and highest values
        if avg_cit:
            high = max(avg_cit , key=itemgetter(2-1) )
            low = min(avg_cit , key=itemgetter(2-1) )
            # Append a list containing the lowest and highest values to the result list
            final_res.append( [low, high] )
        # If there are no city averages for the current category, append None to the result list
        else:
            final_res.append(None)
    # Return the result list
    return  final_res

    # TA help with the function on 4/1/2023

def display_statistics(col, data, cities):
    """
    Display statistics for a given column in a data set or each city.
    Parameers:
    col (int): The index of the column to display statitics for.
    daa (list): A list of liss representing the data set.
    cities (list): A list of city names corresponding to the rows in the data set.
    Returns: None
    This function calculates and displays the minimum, maximum, averag, and modes for the given
    column for each city in the deired format.
    """
    # Get the minimum, maximum, average, and modes for the given column for each city
    avg_nums = get_average(col , data , cities)
    max_nums = get_max(col , data , cities)
    modes_nums = get_modes(col , data , cities)    
    min_nums = get_min(col , data , cities)
    # Print the results for each city in the desired format
    for l,  place in enumerate(cities):
        print("\t{}: ".format(place))
        # Print the minimum value
        print("\tMin: {:.2f}".format(min_nums [l][1] ) , end=" ")
        # Print the maximum value
        print("Max: {:.2f}".format(max_nums [l][1] ) , end=" ")
        # Print the average value
        print("Avg: {:.2f}".format(avg_nums [l][1] ) )
        # Print the most common repeated values
        # Check if there are any modes for the current city
        if modes_nums [l][1]:
            # Get the list of modes and convert them to strings
            list_123 = modes_nums [l][1]
            mode_strings =  ", ".join(str(k) for k in list_123 )
            # Get the number of occurrences for the most common mode
            occur = modes_nums [l][2]
            # Create a formatted string that includes the number of occurrences and the mode values
            out = "\tMost common repeated values ({:d} occurrences): {}\n".format(occur , mode_strings )
            # Print the formatted string
            print(out)
        else:
            # If there are no modes, print a message indicating that
            print("\tNo modes.")

def main():
    """
    Main funcion of the program. Displays a menu of options for the user to choose from, and peforms various statistical 
    analyses on climate data based on user inputs. The available options are:
    1. Find the mximum value for a given category within a specifie date range.
    2. Find the mnimum value for a given category within a specified date range.
    3. Find the average value for a given category within a specified date range.
    4. Find the mode value(s) for a given category within a specified date range.
    5. Display statistics (minimum, maximum, average, and mode) for a given category within a specified date range.
    6. Find the lowest and highest average values for ach category across all data.
    7. Exit the program.
    The program prompts the user for inuts as necessary, and displays the results of the choen analysis. 
    """
    # Print a banner to the console
    print(BANNER)
    # Open the files and get a list of file pointers
    files , pointing = open_files()
    # Read the data from the file pointers into a list of dictionaries
    data = read_files(pointing)
    # Create an empty list to store the names of the cities entered
    cities_entered = []
    # Iterate over the list of file names
    for name_file in files:
        # Remove the file extension from the file name to get the name of the city
        place = name_file[:-4]
        # Add the city name to the list of cities entered
        cities_entered.append(place)

    while True:
        user_choice =  input(MENU)

        if user_choice == '1':
            # get user inputs for start date, end date, and category
            starting = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            cats = input("\nEnter desired category: ").lower()
            # print category name
            print('\n\t{}: '.format(cats))
            # check if category exists
            if cats in COLUMNS:
                # get the max values for the specified category
                data_range =  get_data_in_range(data , starting , ending)
                maximum =  get_max(COLUMNS.index(cats) , data_range , cities_entered)
                # print the max values for each city
                for cittis, value_ in maximum:
                    print("\tMax for {}: {:.2f}".format(cittis , value_))
            else:
                # print an error message if the category doesn't exist
                print("\n\t{} category is not found.".format(cats))

        elif user_choice == '2':
            # get user inputs for start date, end date, and category
            starting = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            cats = input("\nEnter desired category: ").lower()
            # print category name
            print('\n\t{}: '.format(cats))
            # check if category exists
            if cats in COLUMNS:
                # get the min values for the specified category
                data_range = get_data_in_range(data, starting, ending)
                minnimum = get_min(COLUMNS.index(cats) , data_range , cities_entered)
                # print the min values for each city
                for cittis , value_ in minnimum:
                    print("\tMin for {}: {:.2f}".format(cittis , value_))
            else:
                # print an error message if the category doesn't exist
                print("\n\t{} category is not found.".format(cats))

        elif user_choice == '3':
            # get user inputs for start date, end date, and category
            starting = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            cats = input("\nEnter desired category: ").lower()
            # print category name
            print('\n\t{}: '.format(cats))
            # check if category exists
            if cats in COLUMNS:
                # get the average values for the specified category
                data_range = get_data_in_range(data , starting , ending)
                average = get_average(COLUMNS.index(cats) , data_range , cities_entered)
                # print the average values for each city
                for cittis , value_ in average:
                    print("\tAverage for {}: {:.2f}".format(cittis , value_))
            else:
                # print an error message if the category doesn't exist
                print("\n\t{} category is not found.".format(cats))

        elif user_choice == '4':
            # get user inputs for start date, end date, and category
            starting = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            cats = input("\nEnter desired category: ").lower()
            # print category name
            print('\n\t{}: '.format(cats))
            # check if category exists
            if cats in COLUMNS:
                # get the mode values for the specified category
                data_range = get_data_in_range(data , starting , ending)
                modes_ = get_modes(COLUMNS.index(cats) , data_range , cities_entered)
                # print the mode values for each city
                for place , mode_1 , counting in modes_:
                    if mode_1:
                        modes_string =  ", ".join(str(v) for v in mode_1)
                        print("\tMost common repeated values for {} ({:d} occurrences): {}\n".format(place , counting , modes_string))
                    else:
                        print("\tNo modes.")
            else:
                # print an error message if the category doesn't exist
                print("\n\t{} category is not found.".format(cats))

        elif user_choice == '5':
            # get user inputs
            starting =  input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending =  input("\nEnter an ending date (in mm/dd/yyyy format): ")
            # loop until a valid category is entered
            while True:
                cat_1 =  input("\nEnter desired category: ").lower()
                if cat_1 in COLUMNS:
                    break
                else:
                    print("\n\t{} category is not found.".format(cat_1))
            # display selected category and its statistics
            print('\n\t{}: '.format(cat_1))
            data_range = get_data_in_range(data , starting , ending)
            display_statistics(COLUMNS.index(cat_1) , data_range , cities_entered)

        elif user_choice == '6':
            # If user inputs 6, prompt for starting date, ending date, and categories of data to analyze
            starting =  input("\nEnter a starting date (in mm/dd/yyyy format): ")
            ending =  input("\nEnter an ending date (in mm/dd/yyyy format): ")
            cats =  input("\nEnter desired categories seperated by comma: ")
            # Convert category input to lowercase and split into a list
            cats =  cats.lower().split(',')
            # Print the header for the analysis
            print('\nHigh and low averages for each category across all data.')
            # Loop through each category entered by the user
            for cat_2 in cats:
                # If the category is found in the list of available categories:
                if cat_2 in COLUMNS:
                    # Get the index of the category in the list of data columns
                    cat = COLUMNS.index(cat_2)
                    # Get the data within the specified date range
                    data_range = get_data_in_range(data , starting , ending)
                    # Get the average value for each city in the specified data range
                    averageing = get_average(cat , data_range , cities_entered)
                    # Initialize variables for finding the lowest and highest average values
                    low = None
                    low_2 = float('inf')
                    high = None
                    high_2 = float('-inf')
                    # Loop through each city and average value pair
                    for citiees , valuees in averageing:
                        # If the average value is lower than the current lowest, update the lowest
                        if valuees < low_2:
                            low = citiees
                            low_2 = valuees
                        # If the average value is higher than the current highest, update the highest
                        if valuees > high_2:
                            high = citiees
                            high_2 = valuees
                    # Print the lowest and highest average values for the category
                    print('\n\t{}: '.format(cat_2))
                    print("\tLowest Average: {} = {:.2f} Highest Average: {} = {:.2f}".format(low , low_2 , high , high_2))
                else:
                    # If the category is not found, print an error message
                    print("\n\t{} category is not found.".format(cat_2))

        elif user_choice == "7":
            # If user inputs 7, print a farewell message and exit the program
            print("\nThank you using this program!")
            break
        else:
            # If user inputs an invalid option, print an error message
            print("\nInvalid choice. Please choose a valid option.\n")

#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()