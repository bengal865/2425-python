# Programmer: Bruce Provencher
# Date: 20 MAY 2016
# Project: Wheat Class 

# Python-style comment 
from crop_class import *

# Potato is a subclass of the Crop class, i.e.
# inherits from the Crop class
class Wheat(Crop):
    """A wheat crop"""
    
    # Constructor
    def __init__(self): # Every class method needs 'self' passed as a parameter
        # Call the parent class constructor with DEFAULT
        # values for wheat
        # growth rate = 1.5; light need = 5; water need = 6
        super().__init__(1,3,6) # Call the superclass/parent class constructor, and pass the values in
        self._type = "Wheat" # Instead of being type generic, type is now set to wheat
        
    # Overriding [polymorphism] grow method for the subclass
    # In other words, changing somewhat how the grow method works/behaves for our new wheat class
    def grow(self, light, water):
        # If you have more and light water than you need, the wheat will grow...
        if light >= self._light_need and water >= self._water_need: 
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5 # grow at 1.5 times the normal growth rate
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.75 # grow at 1.75 times the normal growth rate
            else:
                self._growth += self._growth_rate # grow at normal rate
                
        # Increment days growing
        self._days_growing += 1
        # Update the crop status
        self._update_status()
    

def main():
    # Create a new wheat crop
    wheat_crop = Wheat()
    print (wheat_crop.report())
    # Manually grow the crop
    manual_grow(wheat_crop) # First run
    print (wheat_crop.report())
    manual_grow(wheat_crop) # Second run with updated report
    print (wheat_crop.report())
    
if __name__ == "__main__":
    main()
