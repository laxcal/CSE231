###########################################################
#  Computer Project #4
# Gives user a menu of options to choose from 
# Based on option chosen user can convert initgers to bases
# as well as encode images and decode images of binary text
# If at any point user inputs an intiger or option that doesnt work 
# they will be asked to input another option
# When user is done, press X and will exit program 
###########################################################

'''Program to convert decimal number to another base, convert decimal number from another base,
convert from one representation system to another, encode an image with text, and decode an image.
Includes main function to run program and display menu.'''

MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    
def numtobase( N, B ):
    '''This function changes a decimal number "N" into its base-B equivalent.
    A string of letters representing a single digit from the new base is the output.
    Up until the length of the string is a multiple of 8 the output is left filled with zeros.
    The decimal number to be converted is N (int).
    - B (int): The base into which to translate "N."
    Gives back the string representation of "N" in base "B," result (str).'''
    if N == 0:
        return ""
        # Initialize the result string
    result = ""
    # Loop until N becomes 0
    while N > 0:
         # Calculate the remainder
        remainder = N % B
        # Add the remainder to the result string
        result = str(remainder) + result
        # Make N to be the quotient of N // B
        N = N // B
        # Return the result string filled with 0s to have a length that is a multiple of 8
    return result.zfill(8 - (len(result.zfill(8)) % 8))

def basetonum( S, B ):
    '''Convert a string representation of a number in a given base to its decimal representation.
    S (str): The string representation of a number in base 'B'.
    B (int): The base of the input number.
    int: The decimal representation of the input number.'''
    if S == '':
        return 0
    # If the input string S is not empty
    else:
        # Make the decimal value to 0
        dec = 0
        # Add the input string S with zeros to the left until it has a length of 8, 
        # reverse the string
        S = S.zfill(8)[::-1]
        # Iterate through each character in the string S
        for i in range(len(S)):
            # for each character add its value multiplied by the base raised to the power of its position
            dec += int(S[i]) * (B ** i)
        # return the decimal version of the number
        return dec

def basetobase(B1,B2,s_in_B1):
    '''Convert a string representation of a number from one base to another.
    B1 (int): The base of the input number 's_in_B1'.
    B2 (int): The base to convert the input number to.
    s_in_B1 (str): The string representation of the input number in base 'B1'.
    str: The string representation of the input number in base 'B2'.'''
    decimal = basetonum(s_in_B1, B1)
    return numtobase(decimal, B2)

def encode_image(image,text,N):
    '''Encodes a text message into an image.
    image (str): The input image to be encoded as a string representation.
    text (str): The text message to be encoded into the image.
    N (int): The number of bits used to represent a single pixel in the image.
    Returns The encoded image as a string representation.
    Returns None if the image is not long enough to hold the encoded message.'''
    # Check if image is not empty
    if not image:
        # return an empty string if image not provided
        return ""
    # Check if text is not empty
    if not text:
        # return the image if text not provided
        return image
    # Check if length of image divided by N is less than length of text times 8
    if len(image) / N < len(text) * 8:
        # return None if image is not long enough to store text
        return None
    # Convert the text into binary representation
    binary1 = ''.join(format(ord(c), '08b') for c in text)
    # Initiaize an empty string to store the encoded image
    encoded = ''
    # Counter variable to iterate through the image
    i = 0
    # Loop until the end of the image
    while i < len(image):
        # Get the next N bytes of the image
        pixel = image[i:i+N]
        # Increment the counter by N
        i = i + N
        # Get the lsb of the pixel
        lsb = pixel[-1]
        # Check if there is still text to encode
        if binary1:
            # Get the next character from the binary of text
            new_lsb = binary1[0]
            # Remove the encoded character from the binary of text
            binary1 = binary1[1:]
        else:
            # Use the original lsb if there is no more text to encode
            new_lsb = lsb
        # Add the pixel with the new lsb to the encoded image
        encoded += pixel[:-1] + new_lsb
    # Return the encoded image
    return encoded

def decode_image(sego,N):
    '''This function decodes a text message that was encoded into an image.
    sego (str): The encoded image as a string representation.
    N (int): The number of bits used to represent a single pixel in the image.
    Returns the decoded text message (str).'''
    # Make an empty string to store the binary version of the decoded text
    text_bin = ''

    # Make an empty string to store the decoded text
    decode = ''

    # Loop through sego in steps of N
    for i in range(0, len(sego), N):
        # Get the next N bytes of the encoded image
        pixelz = sego[i:i+N]
        # Add the lsb of the pixel to the binary version of the text
        text_bin += pixelz[-1]
        # Check if the binary version is 8 bits long
        if len(text_bin) >= 8:
            # Decode the next 8 bits into a character
            decode += chr(int(text_bin[:8], 2))
            # Remove the decoded 8 bits from the binary version of the text
            text_bin = text_bin[8:]

    # Return the decoded text
    return decode



def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    print(MENU)
    choice = input("\n\tEnter option: ").upper()
    # The program enters a loop, which only stops when the user selects option 'X'.
    while choice != 'X':

        if choice == 'A':
            while True:
                N = float(input("\n\tEnter N: "))
                # Checks for an intiger greater than 0
                if N < 0: 
                    print(f"\n\tError: {int(N)} was not a valid non-negative integer.")
                elif N % 1 != 0:
                    print(f"\n\tError: {N} was not a valid non-negative integer.")
                else:
                    # Will use an intiger if it meets the criteria needed
                    N = int(N)
                    break
            while True:
                B = int(input("\n\tEnter Base: "))
                if 2 <= B <= 10:
                    break
                else:
                    #Needs to be an intiger between 2 and 10 or else error
                    print(f"\n\tError: {B} was not a valid integer between 2 and 10 inclusive.")
            print(f"\n\t {N} in base {B}: {numtobase(N, B)}")

        elif choice == 'B':
            S = input("\n\tEnter string number S: ")
            while True:
                # Needs to be an intiger between 2 and 10 
                B = int(input("\n\tEnter Base: "))
                if 2 <= B <= 10:
                    break
                else:
                    print(f"\n\tError: {B} was not a valid integer between 2 and 10 inclusive.")
            print(f"\n\t {S} in base {B}: {basetonum(S, B)}")

        elif choice == 'C':
            while True:
                B1 = int(input("\n\tEnter base B1: "))
                if 2 <= B1 <= 10:
                    break
                else:
                    # Needs to be an intiger between 2 and 10 for base 1 
                    print(f"\n\tError: {B1} was not a valid integer between 2 and 10 inclusive.")
            while True:
                # Same deal for base 2. The intiger needs to be between 2 and 10 or else error
                B2 = int(input("\n\tEnter base B2: "))
                if 2 <= B2 <= 10:
                    break
                else:
                    print(f"\n\tError: {B2} was not a valid integer between 2 and 10 inclusive.")
            s_in_B1 = input("\n\tEnter string number: ")
            print(f"\n\t {s_in_B1} in base {B1} is {basetobase(B1,B2,s_in_B1)} in base {B2}...")   
            
        elif choice == 'E':
            # Uses user inputs for the encode process
            image = input("\n\tEnter a binary string of an image: ")
            N = int(input("\n\tEnter number of bits used for pixels: "))
            text = input("\n\tEnter a text to hide in the image: ")
            encoded_image = encode_image(image, text, N)
            if encoded_image:
                # Prints both encoded and original images to see differnece 
                print(f"\n\t Original image: {image}")
                print(f"\n\t Encoded image: {encoded_image}")
            else:
                print("\n\tImage not big enough to hold all the text to steganography")

        elif choice == 'D':
            # Prompts for the user to input the encoded string for the program
            image = input("\n\tEnter an encoded string of an image: ")
            N = int(input("\n\tEnter number of bits used for pixels: "))
            text = decode_image(image, N)
            if text:
                print(f"\n\t Original text: {text}")
            else:
                print(f"\n\t Original text: {text}")
        elif choice == 'M':
            print(MENU)
        else:
            print(f"\nError:  unrecognized option [{choice}]")
            print(MENU)
        choice = input("\n\tEnter option: ").upper()
    print('\nMay the force be with you.')

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
     main()