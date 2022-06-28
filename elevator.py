import time

def print_pause(message):
    print(message)
    time.sleep(1.5)
 
def floorOption():
    print_pause("Please enter the number for the floor you would like to visit:")
    print_pause("1. Lobby \n2. Human resources \n3. Engineering department")
    option = int(input()) 
    return option
    

def intro():
    print_pause( "You have just arrived at your new job!")
    print_pause( "You are in the elevator.")

def elevatorOption(option):
    location= {1:{'first':'lobby'} , 2:{'second':'human resources department'}, 3:{'third':'engineering department'}}
    for primekey, secondkey in location.items():
        for key, value in secondkey:
            if primekey == option:
                print_pause(f'You push the button for the {key} floor.')
                print_pause(f'After a few moments, you find yourself in the {value}.')

def gonext():
    print_pause('Where would you like to go next?')
    floorOption()
               
intro()
while True:
    elevatorOption(floorOption())
    gonext()