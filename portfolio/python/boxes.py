import math
from math import ceil

class BoxesRequired:
    #Define Constructor
    def __init__(self, items_per_box, total_items):
        self.total_items = total_items
        self.items_per_box = items_per_box
        
    #Define function calculate number of boxes needed
    def calculate_boxes(self):
        self.boxes_needed = math.ceil(self.total_items / self.items_per_box)
        return self.boxes_needed
    
#Ask for user input
total_items = int(input('Enter the number of manufactured items: '))
items_per_box = int(input('Enter the number of items to pack per box: '))

#Create an instance of BoxRequired class
boxes_calculator = BoxesRequired(items_per_box, total_items)

#Calculate boxes needed
boxes_needed = boxes_calculator.calculate_boxes()

#Print the result
print(f'The number of boxes necessary to hold the items is: {boxes_needed}')