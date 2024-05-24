# Arbitrary keywords arguments
def build_profile(fname, lname, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    user_info['first_name'] = fname
    user_info['last_name'] = lname
    return user_info


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)
