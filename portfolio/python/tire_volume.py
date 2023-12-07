import math
import datetime

class CarTire:
    def __init__(self, width, aspect_ratio, diameter):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.diameter = diameter

    def calculate_volume(self):
        # Convert the width from millimeters to meters
        width_in_meters = self.width / 1000

        # Calculate the volume in cubic meters using the provided formula
        pi = math.pi
        volume = (pi * (self.width**2) * self.aspect_ratio * (self.width * self.aspect_ratio + 2540 * self.diameter)) / 10000000000
        
        # Return the calculated volume in liters
        return volume

class Date_Time:
    
    def get_current_date():
        # Get the current date
        today = datetime.datetime.today()
        return today.strftime("%Y-%m-%d")

class File:
    @staticmethod
    def file_txt(current_date, width, aspect_ratio, diameter, volume, price, phone_number):
        with open('Volumes.txt', 'a') as file:
            file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume}, ${price}, {phone_number}\n")

class Tire_Prices:
    def __init__(self):
        # Define a dictionary to store tire sizes and their prices
        self.tire_prices = {
            (205, 60, 15): 100,   # Example: (Width, Aspect Ratio, Diameter): Price
            (215, 65, 16): 120,
            (225, 55, 17): 140,
            (185, 50, 14): 90,
            
        }

    def get_price(self, tire_size):
        # Check if the tire size is in the dictionary and return the price
        return self.tire_prices.get(tire_size)

class Buyers_Choice:
    def buy_tire(self):
        # Prompt the user to input tire specifications
        width = int(input("Enter the tire width in millimeters: "))
        aspect_ratio = int(input("Enter the aspect ratio: "))
        diameter = int(input("Enter the wheel diameter in inches: "))

        # Create a CarTire object with the provided specifications
        tire = CarTire(width, aspect_ratio, diameter)

        # Calculate the volume in liters
        volume_liters = tire.calculate_volume()

        # Get the price for the tire size
        tire_sizes = (width, aspect_ratio, diameter)
        tire_prices = Tire_Prices()
        price = tire_prices.get_price(tire_sizes)

        if price is not None:
            print(f"The price for the selected tire size is ${price}.")
        else:
            print("Sorry, we don't have pricing information for the selected tire size.")

        # Collect the user's phone number
        phone_number = input("Please enter your phone number: ")

        # Get the current date
        current_date = Date_Time.get_current_date()

        # Write the details to a file
        file_handler = File()
        file_handler.file_txt(current_date, width, aspect_ratio, diameter, volume_liters, price, phone_number)

        print(f"The volume of the tire is approximately {volume_liters:.2f} liters.")

    def decide_to_buy(self):
        buy_tires = input("Do you want to buy tires with these dimensions? (yes/no): ")
        if buy_tires.lower() == "yes":
            self.buy_tire()
        elif buy_tires.lower() == "no":
            print('Offer not accepted')
        else:
            print('Invalid input. Please enter "yes" or "no".')

# Check if the script is executed as the main program
if __name__ == "__main__":
    buyer = Buyers_Choice()
    buyer.decide_to_buy()