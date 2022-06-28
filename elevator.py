import time

# Create print function that receives message as param. Pause 1.5 sec after every printed line 
def print_pause(message):
    print(message)
    time.sleep(1.5)

#Display floor option menu, get user input and retun it 
def floorOption():
    print_pause("Please enter the number for the floor you would like to visit:")
    print_pause("1. Lobby \n2. Human resources \n3. Engineering department")
    option = int(input()) 
    return option
    
# First lines of introduction to the elevator program
def intro():
    print_pause( "You have just arrived at your new job!")
    print_pause( "You are in the elevator.")

#Accepts user's input as parameter from floorOpttion() and get values accordingly within a nested dictionary
def elevatorOption(option):
    #location nested distionary key-pair-values
    location= {1:{'first':'lobby'}, 
               2:{'second':'human resources department'}, 
               3:{'third':'engineering department'}}
    for primekey, secondkey in location.items():
        for key in secondkey:
            # Primekey number is compared with the parameter's value passed, "option" (user's input)
            if primekey == option:
                print_pause(f'You push the button for the {key} floor.')
                print_pause(f'After a few moments, you find yourself in the {secondkey[key]}.')

# Displays the "where to go next" question.
def gonext():
    print_pause('Where would you like to go next?')

# (Main) Function that starts the program               
def start():
    intro()
    while True:
        elevatorOption(floorOption())
        gonext()

# Function call to begin the elevator simulation program
start()
