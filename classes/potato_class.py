# Programmer: Bruce Provencher
# Date: 20 MAY 2016
# Project: Potato Class 

# Python-style comment 
from crop_class import *

# Potato is a subclass of the Crop class, i.e.
# inherits from the Crop class
class Potato(Crop):
    """A potato crop"""
    
    # Constructor
    def __init__(self): # Every class method needs 'self' passed as a parameter
        # Call the parent class constructor with DEFAULT
        # values for potato
        # growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6) # Call the superclass/parent class constructor, and pass the values in
        self._type = "Potato" # Instead of being type generic, type is now set to potato
        
    # Overriding [polymorphism] grow method for the subclass
    # In other words, changing somewhat how the grow method works/behaves for our potato class
    def grow(self, light, water):
        # If you have more and light water than you need, potato will grow...
        if light >= self._light_need and water >= self._water_need: 
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5 # grow at 1.5 times the normal growth rate
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25 # grow at 1.25 times the normal growth rate
            else:
                self._growth += self._growth_rate # grow at normal rate
                
        # Increment days growing
        self._days_growing += 1
        # Update the crop status
        self._update_status()
    

def main():
    # Create a new potato crop
    potato_crop = Potato()
    print (potato_crop.report())
    # Manually grow the crop
    manual_grow(potato_crop) # First run
    print (potato_crop.report())
    manual_grow(potato_crop) # Second run with updated report
    print (potato_crop.report())
    
if __name__ == "__main__":
    main()
