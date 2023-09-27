###########################################################
#  Computer Project #2
#
# This program computes the amount of money a player will be billed from different
# car rental options
#       Input CLASSIFICATION CODE, DAYS RENTED, ODOMETER AT START OF RENT, AND ODOMETER AT END OF RENT
#           Computes the given intigers and prints a customer summary  
#               Does not allow other classification codes than the ones given
#                    Displays closing message when player is done
###########################################################
# Below is the inital prompt it gives the player of what they will enter and asks if the player wants to continue
BANNER = "\nWelcome to Horizons car rentals. "
print(BANNER)
print("\nAt the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")
PROMPT = input('\nWould you like to continue (A/B)? ')
while PROMPT != 'A':
    print('\nThank you for your loyalty.')
    break
while PROMPT == 'A':
    # Below are all inputs the player will enter 
    code = input("\nCustomer code (BD, D, W): ")
    if code == 'BD' or code == 'D' or code == 'W':
        numday = int(input("\nNumber of days: "))
        initalod = int(input("\nOdometer reading at the start: "))
        endod = int(input("\nOdometer reading at the end:   "))
        nummiles = (endod - initalod)
        if endod < initalod:
            nummiles = (1000000 - initalod + endod) / 10 # This is to make sure if the odometer turns over the miles are accounted for correctly
            # Above also takes into account the 10th of the mile that is accounted for. For example not 100000 but actually 10000.0
        else:
            nummiles = (endod - initalod) / 10
    # Below are the three classification codes a player can enter (BD, D, W)
    # The amount the player owes is computerd under the variable "amountdue"
        if code == 'BD':
            amountdue = (40 * numday) + (nummiles * .25) # BD was the simplest with just the days and number of miles both being charged 
        if code == 'D': # D needed to accouunt for if the miles were above 100 and charge them differently
            avgmiles = nummiles / numday
            if avgmiles > 100:
                thisvariable = (nummiles - (numday * 100)) # Thisvariable is the miles that need to be charged 25 cents
                amountdue = (60 * numday) + (thisvariable * .25)
            else:
                amountdue = 60 * numday
        if code == 'W': # W was the most complex becasue it needed to account 
                        # for a basic week charge as well as > 900 miles and < 1500 miles or over 1500 miles
            # Import math allows me to use the math.ceil function for the rounding of weeks
            import math
            weeks = math.ceil(numday / 7) # This make sure the weeks are correct and rounds up to the next week if over a week but not a whole number
            basecharge = weeks * 190
            mileagecharge = nummiles * .25
            weekaverage = (((endod - initalod) / weeks) / 10) # Is average week mileage with the 10th that is at the end of the odometer
            if weekaverage <= 900:
                mileagecharge = 0
                amountdue = mileagecharge + basecharge
            elif weekaverage > 900 and weekaverage < 1500:
                mileagecharge = weeks * 100
                amountdue = mileagecharge + basecharge
            else:
                realmiles = nummiles -(weeks * 1500)
                mileagecharge = (200 * weeks) + (realmiles * .25)
                amountdue = mileagecharge + basecharge
        # Once the amount due has been assesed all of the variables are printed below under the customer summary 
        print("\n\nCustomer summary:")
        print("\tclassification code:", code)
        print("\trental period (days):", numday)
        print("\todometer reading at start:", initalod)
        print("\todometer reading at end:  ", endod)
        print("\tnumber of miles driven: ", nummiles)
        print("\tamount due: $", float(amountdue))
        PROMPT = input('\nWould you like to continue (A/B)? ')
        if(PROMPT) != "A":
         print("\nThank you for your loyalty.") 
    else: # Below is what is printed if a customer code that is not right is input into the code
        print("\n\t*** Invalid customer code. Try again. ***")