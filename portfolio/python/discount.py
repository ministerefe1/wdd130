# Import the datetime module
import datetime

# Define a class named DiscountCalculator
class DiscountCalculator:
    def __init__(self):
        pass

    # Define an instance method to calculate the discount based on the subtotal
    def calculate_discount(self, subtotal):
        # Get the current date
        current_date = datetime.date.today()

        # Get the day of the week as a string (e.g., "Monday", "Tuesday", etc.)
        current_day_of_week = current_date.strftime("%A")

        # Initialize discount percentage
        discount_percentage = 0

        # Check if the subtotal is $50 or greater and it's Tuesday or Wednesday
        if subtotal >= 50 and (current_day_of_week == "Tuesday" or current_day_of_week == "Wednesday"):
            discount_percentage = 0.10  # 10% discount

        return discount_percentage

# Create an instance of the DiscountCalculator class
calculator = DiscountCalculator()

# Get the customer's subtotal as input
input_subtotal = float(input("Please enter the subtotal: "))

# Use the instance method to calculate the discount
discount_percentage = calculator.calculate_discount(input_subtotal)

# Calculate the discount amount
discount_amount = input_subtotal * discount_percentage

# Calculate the subtotal after applying the discount
subtotal_after_discount = input_subtotal - discount_amount

# Calculate sales tax (6%)
sales_tax_rate = 0.06
sales_tax_amount = subtotal_after_discount * sales_tax_rate

# Calculate the total amount due
total_amount_due = subtotal_after_discount + sales_tax_amount

# Display the results
print("Discount Amount: $" + format(discount_amount, ".2f"))
print("Sales Tax Amount: $" + format(sales_tax_amount, ".2f"))
print("Total Amount Due: $" + format(total_amount_due, ".2f"))
