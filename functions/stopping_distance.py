# Bruce Provencher
# 04 MAY 2021
# Stopping Distance Calculator

# This script will estimate the total stopping distance 
# of a vehicle based on its speed

import time

# Create CONSTANTS for this calculation
GRAVITY = 9.81 # In meters/second squared
RESPONSE_TIME = 1.5 # In seconds

def get_speed_in_mph():
    # Get the car's speed in MPH (miles per hour)
    car_speed = float(input('Enter the car\'s speed in miles/hour (Example: 55)\n'))
    return car_speed

def convert_to_meters_per_second(mph):
    # Convert car's speed from MPH to meters per second
    return mph / 2.237

def show_road_conditions():
    # Prompt user for road conditions
    print('Current Road Conditions')
    print('1. Dry')
    print('2. Wet')
    print('3. Icy\n')

    option = int(input('Please select an menu option (1 - 3):\n'))

    if option == 1:
        friction_coefficient = 0.7
    elif option == 2:
         friction_coefficient = 0.5
    elif option == 3:
         friction_coefficient = 0.3
    else:
        print('Invalid selection! Enter 1 - 3 only!')
        show_road_conditions()
    return friction_coefficient
    
def thank_you():
    print('Thank you for using my Stopping Distance Calculator!')
    time.sleep(2)
    print('Goodbye!')

def again():
    calc_again = input('Do you want to perform another calculation? (y/n)\n')
    calc_again = calc_again.lower()
    if calc_again in ['y', 'yes']:
        main()
    elif calc_again in ['n', 'no']:
        thank_you()
    else:
        again()


def calc_reaction_dist(velocity, RESPONSE_TIME):
    reaction_dist = velocity * RESPONSE_TIME
    return reaction_dist

def calc_braking_dist(velocity, friction_coefficient, GRAVITY):
    braking_dist = ((velocity ** 2) / (2 * friction_coefficient * GRAVITY))
    return braking_dist

def calc_stopping_dist(reaction, braking):
    stopping_dist = reaction + braking
    return stopping_dist


def display_output(vehicle_mph, mu, dist_react, dist_brake, dist_stop):
    print(f'Speed (mph): {vehicle_mph:,.1f}')
    print(f'Friction Coefficient: {mu:,.2f}')
    print(f'Reaction Distance (meters): {dist_react:,.1f}')
    print(f'Braking Distance (meters): {dist_brake:,.1f}')
    print(f'Stopping Distance (meters): {dist_stop:,.1f}\n')

def main():
    car_mph = get_speed_in_mph()
    car_meters_per_second = convert_to_meters_per_second(car_mph)
    friction = show_road_conditions()
    react_dist = calc_reaction_dist(car_meters_per_second, RESPONSE_TIME)
    brake_dist = calc_braking_dist(car_meters_per_second, friction, GRAVITY)
    stop_dist = calc_stopping_dist(react_dist, brake_dist)
    
    display_output(car_mph, friction, react_dist, brake_dist, stop_dist)
    
    again() 
    
if __name__ == "__main__":
    main()

