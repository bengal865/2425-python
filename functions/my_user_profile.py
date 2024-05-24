# Bruce Provencher
# My User Profile

def build_my_profile(fname, lname, age, **user_info):
    '''Build a DICTIONARY containing a few facts about me.'''

    user_info['first_name'] = fname
    user_info['last_name'] = lname
    user_info['age'] = age

    return user_info

my_profile = build_my_profile('bruce', 'provencher', 56, citizenship='american', school='career tech', subject='web & app dev')
print(my_profile)








# def describe_my_car(make, model, year, **vehicle_specs):
#     '''Build dictionary containing relevant info about my car.'''
#     vehicle_specs['make'] = make
#     vehicle_specs['model'] = model
#     vehicle_specs['year'] = year
#     return vehicle_specs

# vehicle_specs = describe_my_car('honda', 'civic', '2014', color='silver', num_cylinders=4, tow_package=False)
# print(vehicle_specs)

# for key, value in vehicle_specs.items():
#     print(f'\n{key.upper()}:')
#     print(f'{value}')

