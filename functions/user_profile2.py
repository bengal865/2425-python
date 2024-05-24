# Working with functions and arguments
def build_profile(fname, lname, **acct_info):
    '''Function that creates and displays a user profile.'''
    acct_info['first_name'] = fname
    acct_info['last_name'] = lname
    return acct_info


my_profile = build_profile(
    'Abraham', 'Lincoln', location='Washington, DC', operating_sys='Windows 10')
print(my_profile)
