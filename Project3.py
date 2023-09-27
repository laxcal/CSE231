###########################################################
#  Computer Project #3
#
#  Prompt for user to put in data asked
#    Calculate a mortgae based on the data 
#       Print a mortgage table or end
#           Loop if user wants to make many tables 
#               Unknown location will base on nation average
#                   Display message if user enters unvalid numbers
#                       Line 171-172 explains how the first example of code (unknown location) is copied and used for the rest of the code 
###########################################################   
# 30-year fixed rate mortgage, 30 years * 12 monthly payments
# Below are all of the given values for the specific locations
NUMBER_OF_PAYMENTS = 360
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

continueit = "Y" # To continue entire program when it prompts the user if they want to continue
calisgenius = 'yes' # For the part of the program where it needs to either go to a table or find the sq. footage
koleisgenius = 'no' # This is the second part of the table or sq. footage split
tableprint = 0 # This is for making sure the table print function is 0 when it resets
printmax = 0 # This is for making sure the print max monthly function is 0 when it resets
locationlist = ['Seattle', 'San Francisco', 'Austin', 'East Lansing'] # These are for it is an unknown location when not this list

while continueit == 'Y': # Main while function for the user to continue or end the program as well as inputs for user to enter data below
    print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
    print("\nEnter a value for each of the following items or type 'NA' if unknown ")
    location = input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ")
    max_sq_footage = input("\nWhat is the maximum square footage you are considering? ")
    max_monthly = input("\nWhat is the maximum monthly payment you can afford? ")
    down_payment = input("\nHow much money can you put down as a down payment? ")
    apr = input("\nWhat is the current annual percentage rate? ")   
    if location not in locationlist: # This is the unknown location list for the user to use national averages
        print("\nUnknown location. Using national averages for price per square foot and tax rate.")
        price_per_sq_foot = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT  # This is to make the price per square foot the given value at the top
        tax_rate = AVERAGE_NATIONAL_PROPERTY_TAX_RATE   # This is to make the tax rate the given value at the top
# Below are all of my inputs for the user and what happens if they were to enter 'NA'
       
        if max_sq_footage != "NA":
            max_sq_footage = int(max_sq_footage)    # Max sq. footage to be used in calculations
            calisgenius = "YES" # Brings the user to the table creater if not NA

        elif max_sq_footage == "NA":
            koleisgenius = "NA" #Brings the user to the sq. footage finder if is NA

        if max_monthly == "NA":
            if max_monthly == 'NA' and max_sq_footage == 'NA':
                print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
                break # If neither the sq. footage or the max montly is given it send this error message
            else:
                max_monthly = AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT * max_sq_footage / NUMBER_OF_PAYMENTS
                
                printmax += 1 # This is to print the message below about if the user can or cannot afford the house 
        
        elif max_monthly != "NA":
            max_monthly = int(max_monthly)
            printmax = 0 # This is also for the if or if cannot afford house
        
        if down_payment == "NA":
            down_payment = 0

        elif down_payment != "NA":
            down_payment = int(down_payment)# This is the downpayment ot be used to calculate the data below

        if apr == "NA":
            apr = APR_2023 # This is the national average apr used in calculations
            aprdif = APR_2023 * 100 # aprdif is the displayed apr that is to the tenths not the one sotred for calculations
            aprdif = round(aprdif, 1)   # Rounding the apr 1 decimal place

        elif apr != "NA":
            apr = float(apr) * 0.01 # This is the apr used for calculations if the user enters a number
            aprdif = apr * 100# This is the apr that will be printed to show the user, but not in calculations
            
        if calisgenius == 'YES': # This entire if statement is to give the calcuations for if the user gave suffucient inputs and can calcualte a table
            interest_rate = (apr) / 12# Interest rate to be used in calculations
            cost = max_sq_footage * price_per_sq_foot# Base cost of the house with no tax
            taxes = (cost * tax_rate) / 12# Taxes that are added onto the house cost
            loan_amount = cost - down_payment# This is the loan amount to be used in the table
            
            mortgage_payment = (loan_amount * (interest_rate * (1 + interest_rate) ** NUMBER_OF_PAYMENTS)) / (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)
            # The morgage payment is without taxes what the user is going to pay per month."\" It is shown on the table and in the printed rundown it gives the user below
            monthly_payment = taxes + mortgage_payment# This is the payment that is final after taxes are taken into account
        
        if koleisgenius == "NA": # This entire if statement is for if th user has not given max sq. footage so it finds that number
            
            interest_rate = apr / 12 # Interest rate for calculations
            principal_amount = (max_monthly * (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)) / (interest_rate * ((1 + interest_rate) ** NUMBER_OF_PAYMENTS)) + down_payment # Principal amount to be used in the calculation of the max sq. footage
            max_sq_footage = principal_amount / price_per_sq_foot # How the max sq. footage is calculated using variables above
          
            print(f'\n\nIn {location}, a maximum monthly payment of ${max_monthly:.2f} allows the purchase of a house of {max_sq_footage:.0f} sq. feet for ${principal_amount:.0f}\n\t assuming a 30-year fixed rate mortgage with a ${down_payment:.0f} down payment at {aprdif:.1f}% APR.')        
        # This is the print statement above that shows the max sq. footage a buyer can afford based on their inputs
        
        elif calisgenius == 'YES' and max_monthly >= monthly_payment:
        # This is what is printd below if sufficient data is inputted by the user to calculate the data being used in the table and give the user a montly payment
            print(f'\n\nIn the average U.S. housing market, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:   # This is for if the maximum monthly price is greater than the montly payment the user will be able to buy the house
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you can afford this house.'.format(max_monthly))    # Prints this staement if the user is able to buy the house
                
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')  # The user can specify here if they want to print a table or not 
            # If the user decides not to print a table it will ask them if they want to make another input of data for a new house
            
            if continueprint == 'Y':# This is for the printing of the table because I based if it prints off data valus >= 1 or not
                tableprint += 1
                
        elif calisgenius == 'YES' and max_monthly < monthly_payment:
            # This is the same as above but is for if the user cannot afford the house. Basicaaly"\" all it gives is a statement saying they cant afford it
                #The table is still asked to be printed if the user can or cannot afford the house
            
            print(f'\n\nIn the average U.S. housing market, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you cannot afford this house.'.format(max_monthly)) 
            
            #Below is if the user prompts to print the table whuch means in this case tableprint would be >= 1 is the user pressed 'Y'
                #The table has been formatted to print the numbers in a decending order and show the user their payments
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            if continueprint == 'Y':
                tableprint += 1       
        
        if tableprint >= 1:
            print("\n Month |  Interest  |  Principal  |   Balance    ")
            print("================================================")
            balance = loan_amount 
            for months in range(1, 361):
                interest_payment = balance * interest_rate  # Payment of interent the user will owe every month
                principal_payment = mortgage_payment - interest_payment # This is the principal payment( what is being taken off the loan)
                
                print(f'{months:^7}| ${interest_payment:>9.2f} | ${principal_payment:>10.2f} | ${balance:>11.2f}')
                balance = balance - principal_payment   # This is the inital balance which is used in the first line of the table and everything is subtraced from there
                
        # Below I have all of the variables and zero'd them out because"\" I was having an error with numbers being carried over while running multiple tests        
        interest_rate = 0
        cost = 0
        taxes = 0
        loan_amount = 0
        mortgage_payment = 0
        monthly_payment = 0
        principal_amount = 0
        max_sq_footage = 0
        calisgenius = 0
        koleisgenius = 0
        location = 0
        max_sq_footage = 0
        max_monthly = 0
        down_payment = 0
        apr = 0
        addone = 0
        interest_payment = 0 
        principal_payment = 0
        balance = 0
        continueprint = 0
        tableprint = 0
        printmax = 0
        continueit = input('\nWould you like to make another attempt (Y or N)? ')    
        # This is the continue variable if the user wants to run another set of inputs or not


        # Below are the rest of the locations in the while statement."\" What I did was I copied and pasted my unknown location and was able to change\the location, and that is all for the reat of the code.
        # Once I figured out one location the rest of them have the same proporties so I was able to copy and paste


    #Same as first unkown location detailed example except change in location
    if location == "Seattle":
        price_per_sq_foot = SEATTLE_PRICE_PER_SQ_FOOT
        tax_rate = SEATTLE_PROPERTY_TAX_RATE
    
        if max_sq_footage != "NA":
            max_sq_footage = int(max_sq_footage)
            calisgenius = "YES"
    
        elif max_sq_footage == "NA":
            koleisgenius = "NA"
    
        if max_monthly == "NA":
            if max_monthly == 'NA' and max_sq_footage == 'NA':
                print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
                break
            else:
                max_monthly = SEATTLE_PRICE_PER_SQ_FOOT * max_sq_footage / NUMBER_OF_PAYMENTS
                printmax += 1
        elif max_monthly != "NA":
            max_monthly = int(max_monthly)
            printmax = 0
        if down_payment == "NA":
            down_payment = 0
    
        elif down_payment != "NA":
            down_payment = int(down_payment)
    
        if apr == "NA":
            apr = APR_2023
            aprdif = APR_2023 * 100
            aprdif = round(aprdif, 1)
    
        elif apr != "NA":
            apr = float(apr) * 0.01
            aprdif = apr * 100
            
        if calisgenius == 'YES':
            interest_rate = (apr) / 12
            cost = max_sq_footage * price_per_sq_foot
            taxes = (cost * tax_rate) / 12
            loan_amount = cost - down_payment
            mortgage_payment = (loan_amount * (interest_rate * (1 + interest_rate) ** NUMBER_OF_PAYMENTS)) / (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)
            monthly_payment = taxes + mortgage_payment
        
        if koleisgenius == "NA":
            
            interest_rate = apr / 12 
            principal_amount = (max_monthly * (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)) / (interest_rate * ((1 + interest_rate) ** NUMBER_OF_PAYMENTS)) + down_payment
            max_sq_footage = principal_amount / price_per_sq_foot
          #Same as first unkown location detailed example except change in location
            #Explains after first unknown location example above

            print(f'\n\nIn {location}, a maximum monthly payment of ${max_monthly:.2f} allows the purchase of a house of {max_sq_footage:.0f} sq. feet for ${principal_amount:.0f}\n\t assuming a 30-year fixed rate mortgage with a ${down_payment:.0f} down payment at {aprdif:.1f}% APR.')
                #Same as first unkown location detailed example except chnage in location

        elif calisgenius == 'YES' and max_monthly >= monthly_payment:
        #Same as first unkown location detailed example except change in location
            #Explains after first unknown location example above

            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you can afford this house.'.format(max_monthly))
                
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            
            if continueprint == 'Y':
                tableprint += 1
                
        elif calisgenius == 'YES' and max_monthly < monthly_payment:
        #Same as first unkown location detailed example except change in location
            #Explains after first unknown location example above  

            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you cannot afford this house.'.format(max_monthly)) 
            
            
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            #Same as first unkown location detailed example except change in location
                #Explains after first unknown location example above

            if continueprint == 'Y':
                tableprint += 1
            if tableprint >= 1:
                print("\n Month |  Interest  |  Principal  |   Balance    ")
                print("================================================")
                balance = loan_amount 
                for months in range(1, 361):
                    interest_payment = balance * interest_rate 
                    principal_payment = mortgage_payment - interest_payment
                    
                    print(f'{months:^7}| ${interest_payment:>9.2f} | ${principal_payment:>10.2f} | ${balance:>11.2f}')
                    balance = balance - principal_payment
                    #Same as first unkown location detailed example except chanage in location
                        #Explains after first unknown location example above

        interest_rate = 0
        cost = 0
        taxes = 0
        loan_amount = 0
        mortgage_payment = 0
        monthly_payment = 0
        principal_amount = 0
        max_sq_footage = 0
        calisgenius = 0
        koleisgenius = 0
        location = 0
        max_sq_footage = 0
        max_monthly = 0
        down_payment = 0
        apr = 0
        addone = 0
        interest_payment = 0 
        principal_payment = 0
        balance = 0
        continueprint = 0
        tableprint = 0 
        printmax = 0
        continueit = input('\nWould you like to make another attempt (Y or N)? ')    
        #Same as first unkown location detailed example except change in location
            #Explains after first unknown location example above

    if location == "San Francisco":
        price_per_sq_foot = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        tax_rate = SAN_FRANCISCO_PROPERTY_TAX_RATE
    
        if max_sq_footage != "NA":
            max_sq_footage = int(max_sq_footage)
            calisgenius = "YES"
    
        elif max_sq_footage == "NA":
            koleisgenius = "NA"
    
        if max_monthly == "NA":
            if max_monthly == 'NA' and max_sq_footage == 'NA':
                print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
                break
            else:
                max_monthly = SAN_FRANCISCO_PRICE_PER_SQ_FOOT * max_sq_footage / NUMBER_OF_PAYMENTS
                printmax += 1
        elif max_monthly != "NA":
            max_monthly = int(max_monthly)
            printmax = 0
        if down_payment == "NA":
            down_payment = 0
    
        elif down_payment != "NA":
            down_payment = int(down_payment)
    
        if apr == "NA":
            apr = APR_2023
            aprdif = APR_2023 * 100
            aprdif = round(aprdif, 1)
    
        elif apr != "NA":
            apr = float(apr) * 0.01
            aprdif = apr * 100
            
        if calisgenius == 'YES':
            interest_rate = (apr) / 12
            cost = max_sq_footage * price_per_sq_foot
            taxes = (cost * tax_rate) / 12
            loan_amount = cost - down_payment
            mortgage_payment = (loan_amount * (interest_rate * (1 + interest_rate) ** NUMBER_OF_PAYMENTS)) / (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)
            monthly_payment = taxes + mortgage_payment
        
        if koleisgenius == "NA":
            
            interest_rate = apr / 12 
            principal_amount = (max_monthly * (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)) / (interest_rate * ((1 + interest_rate) ** NUMBER_OF_PAYMENTS)) + down_payment
            max_sq_footage = principal_amount / price_per_sq_foot
        #Same as first unkown location detailed example except chanage in location
            #Explains after first unknown location example above

            print(f'\n\nIn {location}, a maximum monthly payment of ${max_monthly:.2f} allows the purchase of a house of {max_sq_footage:.0f} sq. feet for ${principal_amount:.0f}\n\t assuming a 30-year fixed rate mortgage with a ${down_payment:.0f} down payment at {aprdif:.1f}% APR.')
            #Same as first unkown location detailed example except chanage in location
                #Explains after first unknown location example above

        elif calisgenius == 'YES' and max_monthly >= monthly_payment:
           
            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you can afford this house.'.format(max_monthly))
                #Same as first unkown location detailed example except chanage in location
    
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            
            if continueprint == 'Y':
                tableprint += 1
                
        elif calisgenius == 'YES' and max_monthly < monthly_payment:
            
            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you cannot afford this house.'.format(max_monthly)) 
            
            
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            if continueprint == 'Y':
                tableprint += 1
                #Same as first unkown location detailed example except chanage in location
                    #Explains after first unknown location example above

        if tableprint >= 1:
            print("\n Month |  Interest  |  Principal  |   Balance    ")
            print("================================================")
            balance = loan_amount 
            for months in range(1, 361):
                interest_payment = balance * interest_rate 
                principal_payment = mortgage_payment - interest_payment
                
                print(f'{months:^7}| ${interest_payment:>9.2f} | ${principal_payment:>10.2f} | ${balance:>11.2f}')
                balance = balance - principal_payment     
                    #Same as first unkown location detailed example except chanage in location
                        #Explains after first unknown location example above
     
        interest_rate = 0
        cost = 0
        taxes = 0
        loan_amount = 0
        mortgage_payment = 0
        monthly_payment = 0
        principal_amount = 0
        max_sq_footage = 0
        calisgenius = 0
        koleisgenius = 0
        location = 0
        max_sq_footage = 0
        max_monthly = 0
        down_payment = 0
        apr = 0
        addone = 0
        interest_payment = 0 
        principal_payment = 0
        balance = 0
        continueprint = 0
        tableprint = 0
        printmax = 0
        continueit = input('\nWould you like to make another attempt (Y or N)? ')    
        #Same as first unkown location detailed example except chanage in location
            #Explains after first unknown location example above

    if location == "Austin":
        price_per_sq_foot = AUSTIN_PRICE_PER_SQ_FOOT
        tax_rate = AUSTIN_PROPERTY_TAX_RATE
    
        if max_sq_footage != "NA":
            max_sq_footage = int(max_sq_footage)
            calisgenius = "YES"
    
        elif max_sq_footage == "NA":
            koleisgenius = "NA"
    
        if max_monthly == "NA":
            if max_monthly == 'NA' and max_sq_footage == 'NA':
                print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
                break
            else:
                max_monthly = AUSTIN_PRICE_PER_SQ_FOOT * max_sq_footage / NUMBER_OF_PAYMENTS
                printmax += 1
        elif max_monthly != "NA":
            max_monthly = int(max_monthly)
            printmax = 0
        if down_payment == "NA":
            down_payment = 0
    
        elif down_payment != "NA":
            down_payment = int(down_payment)
    
        if apr == "NA":
            apr = APR_2023
            aprdif = APR_2023 * 100
            aprdif = round(aprdif, 1)
    
        elif apr != "NA":
            apr = float(apr) * 0.01
            aprdif = apr * 100
            
        if calisgenius == 'YES':
            interest_rate = (apr) / 12
            cost = max_sq_footage * price_per_sq_foot
            taxes = (cost * tax_rate) / 12
            loan_amount = cost - down_payment
            mortgage_payment = (loan_amount * (interest_rate * (1 + interest_rate) ** NUMBER_OF_PAYMENTS)) / (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)
            monthly_payment = taxes + mortgage_payment
        
        if koleisgenius == "NA":
            
            interest_rate = apr / 12 
            principal_amount = (max_monthly * (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)) / (interest_rate * ((1 + interest_rate) ** NUMBER_OF_PAYMENTS)) + down_payment
            max_sq_footage = principal_amount / price_per_sq_foot
            #Same as first unkown location detailed example except chanage in location
                #Explains after first unknown location example above

            print(f'\n\nIn {location}, a maximum monthly payment of ${max_monthly:.2f} allows the purchase of a house of {max_sq_footage:.0f} sq. feet for ${principal_amount:.0f}\n\t assuming a 30-year fixed rate mortgage with a ${down_payment:.0f} down payment at {aprdif:.1f}% APR.')
        
        elif calisgenius == 'YES' and max_monthly >= monthly_payment:
        #Same as first unkown location detailed example except chanage in location
            #Explains after first unknown location example above

            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you can afford this house.'.format(max_monthly))
                
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            
            if continueprint == 'Y':
                tableprint += 1
                
        elif calisgenius == 'YES' and max_monthly < monthly_payment:
        #Same as first unkown location detailed example except chanage in location
            #Explains after first unknown location example above

            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you cannot afford this house.'.format(max_monthly)) 
            
            
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            if continueprint == 'Y':
                tableprint += 1  
                #Same as first unkown location detailed example except chnage in location
                    #Explains after first unknown location example above

        if tableprint >= 1:
            print("\n Month |  Interest  |  Principal  |   Balance    ")
            print("================================================")
            balance = loan_amount 
            for months in range(1, 361):
                interest_payment = balance * interest_rate 
                principal_payment = mortgage_payment - interest_payment
                
                print(f'{months:^7}| ${interest_payment:>9.2f} | ${principal_payment:>10.2f} | ${balance:>11.2f}')
                balance = balance - principal_payment
                    #Same as first unkown location detailed example except chanage in location

        interest_rate = 0
        cost = 0
        taxes = 0
        loan_amount = 0
        mortgage_payment = 0
        monthly_payment = 0
        principal_amount = 0
        max_sq_footage = 0
        calisgenius = 0
        koleisgenius = 0
        location = 0
        max_sq_footage = 0
        max_monthly = 0
        down_payment = 0
        apr = 0
        addone = 0
        interest_payment = 0 
        principal_payment = 0
        balance = 0
        continueprint = 0
        tableprint = 0
        printmax = 0
        continueit = input('\nWould you like to make another attempt (Y or N)? ')    
        #Same as first unkown location detailed example except chanage in location
            #Explains after first unknown location example above

    if location == "East Lansing":
        price_per_sq_foot = EAST_LANSING_PRICE_PER_SQ_FOOT
        tax_rate = EAST_LANSING_PROPERTY_TAX_RATE
    
        if max_sq_footage != "NA":
            max_sq_footage = int(max_sq_footage)
            calisgenius = "YES"
    
        elif max_sq_footage == "NA":
            koleisgenius = "NA"
    
        if max_monthly == "NA":
            if max_monthly == 'NA' and max_sq_footage == 'NA':
                print("\nYou must either supply a desired square footage or a maximum monthly payment. Please try again.")
                break
            else:
                max_monthly = EAST_LANSING_PRICE_PER_SQ_FOOT * max_sq_footage / NUMBER_OF_PAYMENTS
                printmax += 1
            
        elif max_monthly != "NA":
            max_monthly = int(max_monthly)
            printmax = 0
            
        if down_payment == "NA":
            down_payment = 0
    
        elif down_payment != "NA":
            down_payment = int(down_payment)
    
        if apr == "NA":
            apr = APR_2023
            aprdif = APR_2023 * 100
            aprdif = round(aprdif, 1)
    
        elif apr != "NA":
            apr = float(apr) * 0.01
            aprdif = apr * 100
            
        if calisgenius == 'YES':
            interest_rate = (apr) / 12
            cost = max_sq_footage * price_per_sq_foot
            taxes = (cost * tax_rate) / 12
            loan_amount = cost - down_payment
            mortgage_payment = (loan_amount * (interest_rate * (1 + interest_rate) ** NUMBER_OF_PAYMENTS)) / (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)
            monthly_payment = taxes + mortgage_payment
        
        if koleisgenius == "NA":
            
            interest_rate = apr / 12 
            principal_amount = (max_monthly * (((1 + interest_rate) ** NUMBER_OF_PAYMENTS) - 1)) / (interest_rate * ((1 + interest_rate) ** NUMBER_OF_PAYMENTS)) + down_payment
            max_sq_footage = principal_amount / price_per_sq_foot
            #Same as first unkown location detailed example except chanage in location
                #Explains after first unknown location example above

            print(f'\n\nIn {location}, a maximum monthly payment of ${max_monthly:.2f} allows the purchase of a house of {max_sq_footage:.0f} sq. feet for ${principal_amount:.0f}\n\t assuming a 30-year fixed rate mortgage with a ${down_payment:.0f} down payment at {aprdif:.1f}% APR.')
        
        elif calisgenius == 'YES' and max_monthly >= monthly_payment:
        #Same as first unkown location detailed example except chanage in location
            #Explains after first unknown location example above

            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you can afford this house.'.format(max_monthly))
                
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            
            if continueprint == 'Y':
                tableprint += 1
                #Same as first unkown location detailed example except chanage in location
                    #Explains after first unknown location example above

        elif calisgenius == 'YES' and max_monthly < monthly_payment:
            
            print(f'\n\nIn {location}, an average {max_sq_footage} sq. foot house would cost ${cost:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${down_payment} at {aprdif:.1f}% APR results\n\tin an expected monthly payment of ${taxes:.2f} (taxes) + ${mortgage_payment:.2f} (mortgage payment) = ${monthly_payment:.2f}')
            if printmax >= 1:
                pass
            else:
                print('Based on your maximum monthly payment of ${:.2f} you cannot afford this house.'.format(max_monthly)) 
                #Same as first unkown location detailed example except chanage in location
                    #Explains after first unknown location example above

            
            continueprint = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
            
            if continueprint == 'Y':
                tableprint += 1  
                #Same as first unkown location detailed example except chanage in location
                    #Explains after first unknown location example above

        if tableprint >= 1:
            print("\n Month |  Interest  |  Principal  |   Balance    ")
            print("================================================")
            balance = loan_amount 
            for months in range(1, 361):
                interest_payment = balance * interest_rate 
                principal_payment = mortgage_payment - interest_payment
                
                print(f'{months:^7}| ${interest_payment:>9.2f} | ${principal_payment:>10.2f} | ${balance:>11.2f}')
                balance = balance - principal_payment         
                #Same as first unkown location detailed example except chanage in location
                    #Explains after first unknown location example above

        interest_rate = 0
        cost = 0
        taxes = 0
        loan_amount = 0
        mortgage_payment = 0
        monthly_payment = 0
        principal_amount = 0
        max_sq_footage = 0
        calisgenius = 0
        koleisgenius = 0
        location = 0
        max_sq_footage = 0
        max_monthly = 0
        down_payment = 0
        apr = 0
        addone = 0
        interest_payment = 0 
        principal_payment = 0
        balance = 0
        continueprint = 0
        tableprint = 0
        printmax = 0
        # This the end of my code and it prompts the user if they want to continue which if they would, would bring them to the top of the while statement.
        continueit = input('\nWould you like to make another attempt (Y or N)? ')