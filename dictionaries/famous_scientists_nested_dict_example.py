# Programmer: Bruce Provencher
# Date: 01 NOV 2016
# Python Nested Dictionaries / Famous Scientists

famous_scientists = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton university'},

    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'},
}

for scientist, scientest_info in famous_scientists.items():
    print("\nScientist's Username: " + scientist)
    full_name = scientest_info['first'] + " " + scientest_info['last']
    location = scientest_info['location']

    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
