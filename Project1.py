    ###########################################################
    #  Computer Project #1
    #  Algorithm
    #    Prompt for an number of rods intiger
    #    Input an integer
    #    Convert input to float 
    #    Input converts individually to METERS, FEET, MILES, and FURLONGS
    #    Prints to the 3rd decimal on all 
    #    Displays Minutes To Walk from equasion
    #    Displays all calculations in order after they are computed
    ###########################################################
var = float(input("Input rods: "))
print("\nYou input",var,"rods.")
print("\nConversions")

    # below are all calculations 
    # 5.0292 was given as how many meters in 1 rod
Meters = var * 5.0292    
Feet = var * 5.0292 / 0.3048
Miles = 5.0292 * var / 1609.34
Furlongs = var / 40
MinutesToWalk = ((Miles / 3.1) * 60)
Rods = (var)

    # print functions display the calculations and outputs at 3 decimal places
print("Meters:",(round(Meters,3)))
print("Feet:", (round(Feet,3)))
print("Miles:", (round(Miles,3)))
print("Furlongs:", (round(Furlongs,3)))
print("Minutes to walk",(round(var,3)),"rods:", (round(MinutesToWalk,3))) 