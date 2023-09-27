#######################################################
# Computer Project #10
#   Algorithm
#       Define a class to represent a stock of cards.
#           Define a class to represent a tableau of cards.
#               Define a class to represent a foundation of cards.
#   Define a class to represent the game.
#       prompt user for a seed value
#           create a shuffled deck of cards using the seed value
#               create a stock of cards using the shuffled deck
#   Create a tableau of cards
#       create a foundation of cards
#           while the game is not over
#               display the game
#   Prompt user for a move
#       if the move is valid, make the move
#           if the move is not valid, print an error message
#               if the game is won, display a message and end the game
#   Display the game and a closing message
########################################################
import cards
RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''
MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game( ):
    """ Docstring:
    Initializes a card game by creating a shuffled deck, dealing cards to 4 players,
    and returning the deck, players' hands, and an empty list for found cards.
    Returns: tuple: A tuple containing the shuffled deck, hands of the players, and an empty list for found cards.
    """
    S_oink = cards.Deck( )  # Create a new deck of cards
    S_oink.shuffle( )  # Shuffle the deck
    tab = [ ]  # Initialize an empty list for players' hands
    for W in range(4):  # Iterate through the 4 players
        tab.append( [ ] )  # Add an empty list for each player's hand
    founds = [ ]  # Initialize an empty list for found cards
    for W in range(4):  # Iterate through the 4 players
        flip = S_oink.deal( )  # Deal one card from the deck
        tab[W].append(flip)  # Add the dealt card to the corresponding player's hand
    return S_oink , tab , founds  # Return the deck, players' hands, and the empty list for found cards

def deal_to_tableau(tableau, stock):
    """ Deals cards from the stock to the tableau.
    This function iterates through the tableau piles and appends a card from
    the stock to each pile, as long as the stock is not empty.
    Args: tableau (list): A list of lists, where each inner list represents a tableau pile.
    stock (Stock object): An object representing the stock of cards.
    Returns: None
    """
    # Iterate through the tableau piles (4 piles in total)
    for Q in range(4):
        # Check if the stock is empty
        if not stock.is_empty( ):
            # Deal a card from the stock
            flip_2 = stock.deal( )
            # Append the dealt card to the current tableau pile
            tableau [Q].append(flip_2)

def validate_move_to_foundation(tableau, from_col):
    ''' Validate whether it is possible to move a card from the given column of the tableau
    to a foundation pile, based on the rules of the game. 
    Args: tableau: list of lists, representing the tableau of cards
    from_col: int, representing the column number of the card to be moved
    Returns: bool: True if the move is valid, False otherwise.
    '''
    if not tableau [from_col]: # check if the column is empty
        print("\nError, empty column:" , from_col + 1)
        return not True # return False if it is
    carding = tableau [from_col] [-1] # get the card from the top of the column
    if carding.rank( ) == 1: # check if the card is an Ace
        print("\nError, cannot move {}.".format(carding) )
        return not True # return False if it is
    not_f_sane = not True
    for item_0 in tableau: # loop through all columns of the tableau
        if item_0: # check if the column is not empty
            final = item_0 [-1] # get the card from the top of the column
            if final.rank( ) == 1 and final.suit( ) == carding.suit( ): # check if there is a foundation pile with the same suit as the card and with a rank of 1
                not_f_sane = True
                break
    if not_f_sane: # if there is a foundation pile with the same suit as the card and with a rank of 1, return True
        return True
    high_S = not True
    for item_1 in tableau: # loop through all columns of the tableau
        if item_1: # check if the column is not empty
            final_1 = item_1 [-1] # get the card from the top of the column
            if carding.rank( ) < final_1.rank( ) and final_1.suit( ) == carding.suit( ): # check if there is a card in any column of the tableau with the same suit as the card and with a higher rank
                high_S = True
                break
    if high_S: # if there is a card in any column of the tableau with the same suit as the card and with a higher rank, return True
        return True
    print("\nError, cannot move {}.".format(carding) ) # if none of the above conditions are met, return False
    return not True

def move_to_foundation(tableau, foundation, from_col):
    '''Moves a card from a column of the tableau to the foundation pile.
    Args: tableau: A list of lists representing the tableau in a game of solitaire. Each list represents a column and 
    contains a series of integers representing cards.
    foundation: A list representing the foundation pile in a game of solitaire. It contains a series of integers 
    representing cards.
    from_col: An integer representing the index of the column in the tableau from which to move a card.
    Returns: None
    '''
    # Check whether the move is valid using the `validate_move_to_foundation` function
    good_or_not = validate_move_to_foundation(tableau , from_col)
    # If the move is valid, move the card from the tableau column to the foundation pile
    if good_or_not:
        movin_0 = tableau [from_col] [-1]  # Get the card to move from the top of the column
        tableau [from_col].remove(movin_0)  # Remove the card from the tableau column
        foundation.append(movin_0)  # Add the card to the foundation pile


def validate_move_within_tableau(tableau, from_col, to_col):
    ''' Check if a move within a tableau is valid or not.
    Parameters:
    tableau (list of lists): Represents the tableau of the solitaire game.
    from_col (int): Represents the index of the column from which a card is being moved.
    to_col (int): Represents the index of the column to which a card is being moved.
    Returns:
    (bool): Returns True if the move is valid, otherwise False.
    '''
    card_is_in = tableau[from_col]   # Check if there is a card in the 'from_col' column.
    if not card_is_in:
        print("\nError, no card in column:" , from_col + 1)   # If there is no card in the 'from_col' column, print an error message.
        return not True   # Return False (i.e., not True) to indicate that the move is invalid.
    return True   # If the function reaches this point, it means that the move is valid. So, return True.
    getting = not tableau [to_col]   # Check if the target column is empty or not.
    if not getting:
        print("\nError, target column is not empty:" , to_col + 1)   # If the target column is not empty, print an error message.
        return not True   # Return False (i.e., not True) to indicate that the move is invalid.

def move_within_tableau(tableau, from_col, to_col):
    ''' Move the top card from the given column in the given tableau to another given column
    if the move is valid according to the rules of the game.
    Parameters:
    tableau (list): A list of lists representing the tableau.
    from_col (int): An integer representing the column index of the card to move from.
    to_col (int): An integer representing the column index to move the card to.
    Returns: None
    Raises: IndexError: if the from_col or to_col index is out of range
    ValueError: if the move is not valid according to the rules of the game.
    '''
    # Validate the move according to the rules of the game
    good_or_not_2 = validate_move_within_tableau(tableau , from_col , to_col)
    # If the move is valid, move the top card from the from_col to the to_col
    if good_or_not_2 == True:
        moving_2 = tableau [from_col] [-1] # get the top card from the from_col
        tableau [from_col].remove(moving_2) # remove it from the from_col
        tableau [to_col].append(moving_2) # append it to the to_col
        

def check_for_win(tableau, stock):
    ''' Check if the game has been won by the player.
    Args: tableau (list): A list of lists representing the tableau of the game.
    stock (obj): An object representing the stock of the game.
    Returns: bool: True if the game has been won, False otherwise.
    '''
    # Check if the stock is empty
    if stock.is_empty( ):
        coubting_2 = 0
        # Initialize counting and coubting_2 variables
        counting = 0
        # Iterate through each item in the tableau
        for item_3 in tableau:
            # Iterate through each card in the item
            for suiting in item_3:
                # Get the rank of the card
                ranks = suiting.rank( )
                # If the rank is 1, increment counting
                if ranks == 1:
                    counting = counting + 1
                # If the rank is not 1, increment coubting_2
                else:
                    coubting_2 = coubting_2 + 1
        none_else = not True
        # Initialize carding_1 and none_else variables
        carding_1 = not True
        # If coubting_2 is 0, set none_else to True
        if coubting_2 == 0:
            none_else = True
        # If counting is 4, set carding_1 to True
        if counting == 4:
            carding_1 = True
        # If carding_1 and none_else are both True, return True
        if none_else and carding_1:
            return True
        # Otherwise, return False
        else:
            return not True
    # If the stock is not empty, return False
    else:
        return not True

def display( stock , tableau , foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''
    print("\n{:<8s}{:^13s}{:s}".format( "stock" , "tableau" , "  foundation"))
    maxm = 0
    for col in tableau:
        if maxm < len(col):
            maxm = len(col)
    assert maxm > 0   # maxm == 0 should not happen in this game?
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format("") , end='')
            else:
                print("{:<8s}".format(" XX") , end='')
        else:
            print("{:<8s}".format("") , end='')        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col [i] ) ), end='' )
        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation [-1] ), end='')
        print()

def get_option( ):
    ''' This function prompts the user to input an option and returns a list based on the input. 
    If the input is one of the pre-defined options, such as 'D', 'R', 'H', or 'Q', then the 
    function returns a list containing only that option. If the input is not one of the 
    pre-defined options but is of the form 'F x' or 'T x y', where x and y are integers 
    between 1 and 4, then the function returns a list with the appropriate command ('F' or 
    'T') and the corresponding integer arguments. If the input is invalid, the function 
    prints an error message and returns an empty list.
    '''
    inputting_in = input("\nInput an option (DFTRHQ): ").strip( )  # Prompt user for input and remove whitespace
    inputting_in_2 = inputting_in.upper( )  # Convert input to all uppercase characters
    if inputting_in_2 == 'Q':  # If the input is 'Q', return a list containing only 'Q'
        return ['Q']
    if inputting_in_2 == 'R':  # If the input is 'R', return a list containing only 'R'
        return ['R']
    if inputting_in_2 == 'H':  # If the input is 'H', return a list containing only 'H'
        return ['H']
    if inputting_in_2 == 'D':  # If the input is 'D', return a list containing only 'D'
        return ['D']
    else:  # If the input is not one of the pre-defined options
        nums = inputting_in_2.split( )  # Split the input into a list of strings
        nums_1 = len(nums)  # Get the length of the list
        if nums_1 == 2:  # If the length of the list is 2
            cording , x = nums  # Assign the two values to variables
            good_or_not_x = x.isdigit( ) and int(x) <= 4 and int(x) >= 1 # Check if x is a valid integer between 1 and 4
            if cording == 'F' and good_or_not_x:  # If the first value is 'F' and x is valid
                return ['F' , int(x) - 1]  # Return a list with 'F' and the integer x minus 1
        if nums_1 == 3:  # If the length of the list is 3
            cording , x , y = nums  # Assign the three values to variables
            good_or_not_x = x.isdigit( ) and int(x) <= 4 and int(x) >= 1 # Check if x is a valid integer between 1 and 4
            good_or_not_y = y.isdigit( ) and int(y) <= 4 and int(y) >= 1 # Check if y is a valid integer between 1 and 4
            if cording == 'T' and good_or_not_x and good_or_not_y:  # If the first value is 'T' and x and y are valid
                return ['T' , int(x) - 1 , int(y) - 1]  # Return a list with 'T' and the integers x and y minus 1
    print("\nError in option: {}".format(inputting_in) )  
    return [ ]

def main( ):
    '''This function runs the main game loop for a game of solitaire. It first prints the rules
    and menu, initializes the game, and then repeatedly prompts the user for input until the
    game is won or the user quits. The user input is used to make moves in the game. If the user
    input is invalid, the loop continues. If the game is won, the function prints a message and
    exits the loop.
    '''
    print(RULES)  # Print the rules of the game
    print(MENU)  # Print the menu
    while True:  # Main game loop
        stoinks, table_1, founding = init_game( )  # Initialize the game
        while not check_for_win(table_1 , stoinks):  # While the game is not won
            display(stoinks , table_1 , founding)  # Display the game state
            picks_0 = get_option( )  # Get user input
            if not picks_0:  # If the input is invalid, continue the loop
                continue
            picks = picks_0 [0]  # Get the first element of the input list
            if picks == 'H':  # If the input is 'H', display the menu
                print(MENU)
            if picks == 'F':  # If the input is 'F', move to foundation
                move_to_foundation(table_1 , founding , picks_0 [1] )
            if picks == 'Q':  # If the input is 'Q', quit the game
                print("\nYou have chosen to quit.")
                return
            if picks == 'D':  # If the input is 'D', deal to tableau
                deal_to_tableau(table_1, stoinks)
            if picks == 'R':  # If the input is 'R', restart the game
                print("=========== Restarting: new game ============")
                break
            if picks == 'T':  # If the input is 'T', move within tableau
                move_within_tableau(table_1 , picks_0 [1] , picks_0 [2] )
        if check_for_win(table_1 , stoinks):  # If the game is won
            print("\nYou won!")  # Print a message
            break  # Exit the loop

if __name__ == '__main__':
     main()