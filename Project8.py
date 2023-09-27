###########################################################
#  Computer Project #8
#
# Define necessary functions for procssing game data
#   Open 'games' and 'discount' files
#       Read the data from the files into dictionaries
#           Display a menu with options to analyze game data
#               Get usr input and perform corresponding analysis
#                   Display analysis results
#                       Repat the menu until the user choses to exit
###########################################################

import csv
from operator import itemgetter

MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''

def open_file(s):
    '''
    Prompts the user t enter the name of a file to be opened for reading.
    If the file is found andcan be opened, the function etuns a file object.
    If the fle is not found, th function prints an error message and prompts the user again.
    If there is an eror opening the file fo any oter reason,the function prints an error message and promts the user again.
    Args: s (str): A string that describes the type of file beingopened, e.g. "input" or "output"
    Returns: oint (file object): A file object that can be used to read the contents of the file.
    '''
    while True:  # Loop until a valid file is opened or the user quits
        try:
            name_of_file = input('\nEnter {} file: '.format(s) )  # Prompt the user for the file name
            point = open(name_of_file , 'r' , encoding='UTF-8')  # Try to open the file for reading
            return point  # If successful, return the file object
        except FileNotFoundError:  # If the file is not found, catch the error and prompt the user again
            print('\nNo Such file')

def look_through_data(line):
    '''
    Parses a sngle line of game data from a CSV file and eturns a tuple containing the game nae and a list of game data.
    Args: line (list: A list of strings containing game data from a single row of a CSV file.
    Returns: Same as read_file(fp_games):
    '''
    # Unpack values from input line
    name_string , release_date_string , dev_list , genre_list , player_mode_int , price_float , overall_reviews_string , reviews_int , percent_positive_int , win_list , mac_list , lin_list = line
    # Check if game has multiplayer mode or not
    if "MULTI-PLAYER" in player_mode_int.upper().split(';') [0]:
        mode__ = 0  # Set mode__ to 0 if game has multiplayer mode
    else:
        mode__ = 1  # Set mode__ to 1 if game doesn't have multiplayer mode
    # Split genre_list and dev_list by semicolons
    genres_list_1 = genre_list.split(';')
    dev_list_2 = dev_list.split(';')
    # Convert price_float to a float and multiply it by 0.012
    try:
        price_float = float(price_float.replace(',' , '') )
        price_float = price_float * 0.012  # Convert the price to USD
    except ValueError:
        price_float = 0.0  # Set price_float to 0.0 if it can't be converted to a float
    # Convert reviews_int to an integer and remove the percentage sign from percent_positive_int
    reviews_int = int(reviews_int)
    percent_positive_int = int(percent_positive_int.replace('%' , '') )
    # Create a list of supported platforms
    supporting = []
    if int(win_list):
        supporting.append('win_support')  # Add 'win_support' to the list if the game supports Windows
    if int(mac_list):
        supporting.append('mac_support')  # Add 'mac_support' to the list if the game supports Mac
    if int(lin_list):
        supporting.append('lin_support')  # Add 'lin_support' to the list if the game supports Linux
    # Return a dictionary containing the game's name and associated data
    return name_string , [release_date_string , dev_list_2 , genres_list_1 , mode__ , price_float , overall_reviews_string , reviews_int , percent_positive_int , supporting]
def read_file(fp_games):
    '''
    Reads data from a CSV file containing information about video games.
    Parses the ata and returns a dictionary of games, wherethe keys are the names of the games and the values are lists of game data.
    Args: fp_games(file object): A file object that has been opened for reading in text mode.
    Returns: diction_of_games (dict):A dictionary of games, where ach key is a game name (str) and each value is a list containing:
    - release_date_string (str): The release date of the game.
    - dev_list_2 (list): A list of developers who worked on the game.
    - genres_list_1 (list): A list of genres that the game belongs to.
    - mode__ (int): A 0 if the gam is multiplayer, or 1 if it is single player.
    - price_foat float): The price of the game.
    - overall_reviews_string (str): The overall review score of the game.
    - reviews_in (int): The number of reviews for the game.
    - percent_poitive_int (int): The percentage of reviews that are positive.
    - support_list (list): A list ofoperating systems that the game supors (win_support, mac_support, lin_support).
    '''
    # Read in a CSV file of game data and create a dictionary of game names and associated data
    fileing = csv.reader(fp_games)
    next(fileing)  # Skip the header row of the CSV file
    diction_of_games = { }
    for item in fileing:
        name_string , dat_in_game = look_through_data(item)  # Convert each row of data into a dictionary containing the game's name and associated data
        diction_of_games[name_string] = dat_in_game  # Add the dictionary to diction_of_games, with the game's name as the key
    return diction_of_games  # Return diction_of_games, which is a dictionary of game names and associated data

def process_rows(fileing):
    '''Reads trugh a CSV file of discounted games and creates a dictionary of game nams and associated discount values.
    Parameters: fileing (csv.reader): A csv.reader object containing the discounted games CSV data.
    Returns:dict_dis (dict): A dictioary of game names ad associated discount values.
    '''
    dict_dis = { }
    for item in fileing:
        name_of_game = item [0]  # Extract the game name from the row
        disc = round(float(item [1] ) , 2)  # Round the discount value from item[1] to two decimal places and return it as a float
        dict_dis[name_of_game] = disc  # Add the game name and discount value to dict_dis
    return dict_dis
def read_discount(fp_discount):
    '''Reads ina SV file of discounted games and creates a dictionary of game names and assoiated discount values.
    Parameters:fp_discount (file object): A file oject containing CSV data of discounted games.
    Returns: dict_dis (dict): A ditionary of game nameand associated discount values.
    '''
    fileing = csv.reader(fp_discount)
    next(fileing)  # Skip the header row of the CSV file
    dict_dis = process_rows(fileing)  # Convert each row of discounted game data into a dictionary containing the game's name and associated discount value
    return dict_dis  # Return dict_dis, which is a dictionary of game names and associated discount values

def in_year(master_D , year):
    '''Return a orted list of game names released in the specified year.
    Parameters master_D (dict): A dictionary containing gamenames and associated data.
    year (int): The yearto filter by.
    Returns: A sorted list of game names released in the specified year.
    '''
    year_games = [ ]
    for name_of_game , info_of_game in master_D.items( ):
        releasing = info_of_game [0]  # Get the release date of the game
        if int(releasing [-4:] ) == year:  # Check if the release year matches the specified year
            year_games.append(name_of_game)  # Add the game name to the list of games released in the specified year
    return sorted(year_games)  # Sort the list of game names and return it

def process_f(name_of_game , information , genre):
    '''Filters games by genre and returs the game name and review score as a tuple if the game matches the specified genre.
    Paramters: name_f_ame (str): The name of the game.
    information (list): A list containing the game's associated data, including release date, developers, genres, multiplayer mode, price, reviews, and supported platforms.
    Returns: tuple: A tuple cntaining the game name and review score if the game mathes the specified genre, otherwise None.
    '''
    if genre in information [2]:  # Check if the specified genre is in the game's list of genres
        return (name_of_game, information[7] )  # Return a tuple containing the game name and review score
    return None
def by_genre(master_D, genre):
    '''Returns a list ofgame names from master_D that match the secified genre, sorted by their review score in descending order.
    Parametrs master_D (dict): A dictionary containing game names and associated data.
    genre (str): A string representing the genrto filter the games by.
    Returns: list: A list of game names that match the specified genre, sorted by review core in descending order.
    '''
    gen_g = [ ]
    for name_of_game , information in master_D.items( ):  # Iterate over each game in master_D
        name__ = process_f(name_of_game, information, genre)  # Process the game using the process_f function to check if it matches the specified genre
        if name__:  # If the game matches the specified genre
            gen_g.append(name__)  # Add the game name and review score to the gen_g list
    sort = sorted(gen_g, key=itemgetter(1), reverse=True)  # Sort the gen_g list by review score in descending order
    finally_1 = [ ]
    for name__ in sort:
        finally_1.append(name__ [0] )  # Add only the game name to the finally_1 list
    return finally_1  # Return a list of game names that match the specified genre, sorted by review score in descending order.

def by_dev(master_D, developer):
    '''Filter a dictionary of games by developer name and retun a list of game titles sorteby release date.
    Args: mase_D (dict): A dictionary containing game titles as keys and lists of game details as values.
    developer (str): The name of the game deeloper to fiter by.
    Returns: list: A list of game titles sorted b release date, filtered by the specified developer.
    '''
    # Create an empty dictionary to hold the filtered games
    game_filter = { }
    # Loop through each game in the master dictionary
    for title, dets in master_D.items( ):
        # Check if the game's developer matches the specified developer
        if developer in dets [1]:
            # If the developer matches, add the game to the filtered dictionary
            game_filter[title] = dets
    def sorting(title):
        '''helper function for sorting game title by release date.
        Args: title (tple): A tuple cntaining a game title and its associated details.
        Returns: str: The release ate of the game in the format "MMDD/YYYY".
        '''
        # Extract the release date from the game's details
        gaming = title [1]
        det_1 = gaming [0]
        det_2 = det_1.split('/')
        det_3 = det_2 [-1]
        # Return the release date in the format "MM/DD/YYYY"
        return det_3
    # Sort the games in the filtered dictionary by release date in descending order
    games_sort = sorted(game_filter.items( ) , key=sorting , reverse=True)
    # Create an empty list to hold the sorted game titles
    final__ = [ ]
    # Loop through each sorted game and append its title to the final list
    for title in games_sort:
        final__.append(title [0] )
    # Return the final list of sorted game titles
    return final__

def calc_dis(g , master_D , discount_D):
        '''
        This function alculates the discounted price for a given gam based on its discount percentage and its original price.
        Parameters: g (sr): The name of the game
        Returns: disc_cost (float): The discounted cost of the game
        '''
        # Get the discount percentage for the game from the discount dictionary
        disc = discount_D[g]
        # Get the original cost of the game from the master dictionary
        cost = master_D[g] [4]
        # Calculate the discounted cost of the game using the discount percentage and the original cost
        disc_cost = round(cost * (1 - disc / 100) , 6)
        # Return the discounted cost of the game
        return disc_cost
def per_discount(master_D , games , discount_D):
    '''
    This function applies discountsto the prices of games in the master dictionary. If a game is listed n the discount dictionary, 
    then the iscou is applied to the price. If not, then the original price is used.
    Parameters: master_D (dict): A dictionarycontaining information about games, where the keys are the names of the games
    games (list): A list of game names for which discounts sholdbe pplied
    discount_D(dct): A dicionary containing discounts for games, where the keys are the names ofthe games and the values 
    re the dscounts as percentages
    Returns: new_price (list): A list of the new discounted prices for the ames
    '''
    new_price = [ ]
    # Iterate through each game and calculate the discounted price
    for g in games:
        if g in discount_D:
            disc_cost = calc_dis(g , master_D , discount_D)  # If the game is listed in the discount dictionary, calculate the discounted price
        else:
            disc_cost = master_D [g] [4]  # If not, use the original price
        new_price.append(disc_cost)  # Add the discounted price to the new_price list
    return new_price  # Return the list of discounted prices

def price_soerted(gis, costs):
        '''Sort th list of game names and associated costs by the cost in ascding order.
        Args: gis (lst): Alist o game names. costs (list): A list of game costs.
        Returns: new_cos_gaame (list): A list of game naes and assoiated costs sorted bythe cost in ascending order.
        '''
        price_new = [ ]
        # Iterate through each game in the list of game names
        for c in range(len(gis) ):
            price_new.append( (gis [c] , costs [c] ) )  # Create a tuple of the game name and its cost after discount, and add it to the list
        new_cost_gaame = sorted(price_new)  # Sort the list of tuples by the cost in ascending order
        return new_cost_gaame

def developer_and_year(master_D, developer, year):
    '''Return a lit of game names developed by the given developer in the given year.
    Returns: new_filter (list): A list of gam names developed by the given developer in the given year.
    '''
    new_filter = [ ]
    # Iterate through each game in the master dictionary
    for g , new_d in master_D.items():
        # Check if the game was developed by the given developer and released in the given year
        if developer in new_d [1] and int(new_d [0] [-4:]) == year:
            new_filter.append(g)  # If so, add the game's name to the list
    return new_filter
def price_soerted(gis , costs):
    '''Sort thlist of game names and associated costs by the cost in ascding order.
    Args: gis (list): A list of game names. costs (list): A list of game costs.
    Returns: new_cos_gaame (list): A list o game naes and associated costs sorted by the cost in ascending order.
    '''
    price_new = [ ]
    # Iterate through each game in the list of game names
    for c in range(len(gis) ):
        price_new.append( (gis [c] , costs [c] ) )  # Create a tuple of the game name and its cost after discount, and add it to the list
    new_cost_gaame = sorted(price_new, key=itemgetter(1) )  # Sort the list of tuples by the cost in ascending order
    return new_cost_gaame
def by_dev_year(master_D , discount_D , developer , year):
    '''Return a list of ames developed by the given developer in the given year, sorted by price after discount.
    Args: master_D (dict): A dictionary containing game names and asscited data.
    - discoun_D (dict):  dictionary containing game names and associated discount percentage.
    - developer(str): A string representing the name of te developer.
    - year (int): An intege representing the year of the ame's release.
    Returns: restting (list): A list of game names developed by the given develoer in the given year, sorted by pice after discount.
    '''
    # Get a list of game names developed by the given developer in the given year
    gis = developer_and_year(master_D , developer , year)
    # Get a list of game costs after discount
    costs = per_discount(master_D , gis , discount_D)
    # Sort the list of game names and associated costs by the cost in ascending order
    new_cost_gaame = price_soerted(gis , costs)
    restting = [ ]
    # Iterate through each game in the list of game names and associated costs
    for g in new_cost_gaame:
        name_game = g [0]
        restting.append(name_game)  # Add the game's name to the list
    return restting  # Return a list of game names developed by the given developer in the given year, sorted by price after discount.

def by_genre_no_disc(master_D , discount_D , genre):
    ''' Returns a list of game names in a specific genre that are not in the discount dictionary, sorted by price and number of reviews.
    Args: aster_D (dict): A dictionarcontaining game information, with game names as keys and game info as values.
    discount_ (dict): A dictionary containing discounted games with game names as keys.
    genre (str): The genre to filter games by.
    Returns: list: A list of game names sorted by price and number of reviews.
    '''
    # Initialize an empty list for games
    g_listing = [ ]
    # Iterate through the games in the master dictionary
    for gn , gi in master_D.items( ):
        # Check if the game is not in the discount dictionary and if the genre matches
        if gn not in discount_D and genre in gi [2]:
            # Add the game name, price, and number of reviews to the list
            gt = (gn , gi [4] , gi [7] )
            g_listing.append(gt)
    # Custom sorting function 
    def other_sort(title):
        ''' Returns a tuple cotaining the price and the negative number of reviews for a given game title.
        Args: title (tple): A tuple containing the game name,price, and number of reviews.
        Returns: tuple: A tuple containing the price and the negative number of reviews.
        '''
        # Extract the second element from the title tuple (price).
        W = title [1]
        # Extract the third element from the title tuple (number of reviews) and negate it.
        W_2 = - title [2]
        # Return a tuple containing the price and negated number of reviews.
        return (W , W_2)
    # Sort the game list (g_listing) by price and number of reviews using the custom sorting key provided by the other_sort function.
    final_s = sorted(g_listing, key=other_sort)
    # Initialize an empty list for the final result.
    last_res = [ ]
    # Loop through the sorted game titles in the final_s list.
    for title in final_s:
        # Extract the game name (the first element of the title tuple).
        gn = title [0]
        # Append the game name to the last_res list.
        last_res.append(gn)
    # Return the last_res list containing the sorted game names based on price and number of reviews.
    return last_res

def by_dev_with_disc(master_D , discount_D , developer):
    ''' Returns a list of game names sorted by their price in ascending order,
    filtered by dveloper and discount information.
    Parameters: master_D (dict): A dictinary of game names and associated data.
    discount_D (dict): A dictionary of discounted game names and prices.
    developer (str): The name of the developer to filter by.
    Returns: list: A list of gamenames sorted by their price in ascending order,
    filtered by developer and discount information.
    '''
    # Initialize an empty list for storing game names and their associated discount values.
    l_ing = [ ]
    # Loop through all items (game names and associated information) in the master_D dictionary.
    for gn , gi in master_D.items( ):
        # Check if the game name exists in the discount_D dictionary and the developer name is in the game information list.
        if gn in discount_D and developer in gi [1]:
            # If both conditions are met, append a tuple containing the game name and the discount value to the l_ing list.
            l_ing.append( (gn , gi [4] ) )
    # Sort the l_ing list using the discount values (the second element of each tuple).
    sorts = sorted(l_ing , key=itemgetter(1) )
    # Initialize an empty list for storing the final result (sorted game names).
    final_res = [ ]
    # Loop through the sorted tuples in the sorts list.
    for g in sorts:
        # Append the game name (the first element of the tuple) to the final_res list.
        final_res.append(g [0] )
    # Return the final_res list containing the sorted game names.
    return final_res


def main():
    '''Main function tht reads in data from 'games' and 'discount'files, presents a menu with options to the user, 
    and then calls appropriate functions bsed on user's input. The function accepts noparamete and returns nothing.'''
    # Open the 'games' and 'discount' files and read in the data
    game_disc = open_file("games")  # Get the file object for 'games'
    master_D = read_file(game_disc)  # Read the data from 'games' into a dictionary
    disc_fp = open_file("discount")  # Get the file object for 'discount'
    discount_D = read_discount(disc_fp)  # Read the data from 'discount' into a dictionary
    while True:  # repeat the menu until user chooses to exit
        try:
            user_options = int(input(MENU) )  # display the menu and get user input as an integer
            # option 1: find games released in a certain year
            if user_options == 1:
                while True:
                    try:
                        year_num = int(input('\nWhich year: ') )  # ask for the year as input
                        break
                    except (ValueError , FileNotFoundError):
                        print("\nPlease enter a valid year")  # handle invalid input
                        continue
                gaming=in_year(master_D , year_num)  # find games released in the given year
                if gaming:
                    print(f"\nGames released in {year_num}:\n{', '.join(gaming)}")  # display games found
                else:
                    print("\nNothing to print")  # no games found
            # option 2: find games made by a certain developer
            elif user_options == 2:
                devs=input('\nWhich developer: ')  # ask for developer's name as input
                gaming=by_dev(master_D , devs)  # find games made by the developer
                if gaming:
                    print(f"\nGames made by {devs}:\n{', '.join(gaming)}")  # display games found
                else:
                    print("\nNothing to print")  # no games found
            # option 3: find games of a certain genre
            elif user_options == 3:
                ganres=input('\nWhich genre: ')  # ask for genre as input
                gaming=by_genre(master_D , ganres)  # find games of the given genre
                if gaming:
                    print(f"\nGames with {ganres} genre:\n{', '.join(gaming)}")  # display games found
                else:
                    print("\nNothing to print")  # no games found
            # option 4: find games made by a certain developer in a certain year
            elif user_options == 4:
                while True:
                    try:
                        devs=input('\nWhich developer: ')  # ask for developer's name as input
                        year_num=int(input('\nWhich year: ') )  # ask for year as input
                        break
                    except ValueError:
                        print("\nPlease enter a valid year")  # handle invalid input
                        continue
                gaming=by_dev_year(master_D , discount_D , devs , year_num)  # find games made by the developer in the given year
                if gaming:
                    print(f"\nGames made by {devs} and released in {year_num}:\n{', '.join(gaming)}")  # display games found
                else:
                    print("\nNothing to print")  # no games found
            # option 5: find games of a certain genre that do not offer any discount
            elif user_options == 5:
                ganres=input('\nWhich genre: ')  # ask for genre as input
                gaming=by_genre_no_disc(master_D , discount_D , ganres)  # find games of the given genre that do not offer any discount
                if gaming:
                    print(f"\nGames with {ganres} genre and without a discount:\n{', '.join(gaming)}")  # display games found
                else:
                    print("\nNothing to print")  # no games found
            elif user_options == 6:
                # Option 6: ask for developer's name
                devs=input('\nWhich developer: ')
                # call function by_dev_with_disc to find the games made by the developer with discount
                gaming=by_dev_with_disc(master_D , discount_D , devs)
                if gaming:
                    # if there are games, print them out
                    print(f"\nGames made by {devs} which offer discount:\n{', '.join(gaming)}")
                else:
                    # if there are no games, print a message indicating nothing to print
                    print("\nNothing to print")
            elif user_options == 7:
                # Option 7: print thank you message and break out of the loop
                print("\nThank you.")
                break
            else:
                # if user enters invalid option, print a message and continue the loop
                print("\nInvalid option")
                continue
        except ValueError:
            # catch any other ValueErrors that might occur and print a message, then continue the loop
            print("\nInvalid option")
            continue
if __name__ == "__main__":
    main()