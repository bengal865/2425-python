# Programmer:Cameron Urban
# Date: 28 APRIL 2021
# Project: Alien Class Evidence

# Make the class
class Alien:
    ''' A class describing the alien character you create, based on what crimes they have committed.'''
    def __init__(self,fname, felonies, clan, global_status):
        self.fname = fname
        self.felonies = felonies
        self.clan = clan
        self.global_status = global_status
    
    def describe(self):
        print(f'Name: {self.fname} \nClan: {self.clan} \nFelonies Committed: {self.felonies} \nGlobal Status: {self.global_status}\n')
    
    def tax_fraud(self):
        print(f'{self.fname} has comitted tax fraud.\n')
        
    def law_abiding(self):
        print(f'{self.fname}, despite being an alien, is on good terms with the FBI.\n')

# Create instances        
zambles = Alien('Zambles','Too many to count', 'Intergalactic Tax Evaders', 'Wanted by the FBI')
space_gerald = Alien('Space Gerald', 0, 'Intergalactic Law Abiders', 'Ignored by the Government')

# Call functions using instances 
zambles.describe()
zambles.tax_fraud()
space_gerald.describe()
space_gerald.law_abiding()