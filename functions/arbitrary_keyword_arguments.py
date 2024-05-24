# Arbitrary Keyword Arguments

# build_profile ( ) function expects a first and last name, but
# also allows user to pass as many name/value pairs as they want

# **user_info parameter creates an empty dictionary

# Can access the name/value pairs in the user_info dictionary as 
# you would any Python dictionary

from turtle import color


def build_profile(fname, lname, **user_info):
    '''Creating a dictionary containing all we know about a user.'''
    user_info['first_name'] = fname
    user_info['last_name'] = lname
    return user_info

user_profile = build_profile('bruce', 'provencher', school='career tech', field='programming and web design', age=56, nationality='american')

print(user_profile)


def make_car(manufacturer, model, **car_specs):
    '''Function that stores info about a car in a dictionary.'''
    car_specs['manufacturer'] = manufacturer
    car_specs['model'] = model
    return car_specs

specs_summary = make_car('honda', 'civic lx', color='green', satellite_radio='False', cd_player='True', num_cylinders = 4)
print(specs_summary)