# Working with an arbitrary number of arguments
def make_vehicle(manufacturer, model, **vehicle_summary):
    '''Function that stores info about a car in a dictionary.'''
    vehicle_summary['manufacturer'] = manufacturer
    vehicle_summary['model'] = model
    return vehicle_summary


vehicle = make_vehicle('GMC', 'Sierra', color='gray',
                       long_bed='True', tow_package='True')
print(vehicle)
