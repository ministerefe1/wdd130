# Function to calculate maximum heart rate per minute
def calculate_max_heart_rate(age):
    return 220 - age

# Function to calculate target heart rate range
def calculate_target_heart_rate_range(max_heart_rate):
    lower_range = 0.65 * max_heart_rate
    upper_range = 0.85 * max_heart_rate
    return lower_range, upper_range

# Function to display the target heart rate range
def display_target_heart_rate_range(lower_range, upper_range):
    print(f"When you exercise to strengthen your heart, you should keep your heart rate between {lower_range} and {upper_range} beats per minute.")
  
# Prompt the user to input their age.
user_age = int(input("Please enter your age: "))

# Calculate the maximum heart rate per minute.
max_heart_rate = calculate_max_heart_rate(user_age)

# Calculate the target heart rate range.
lower_range, upper_range = calculate_target_heart_rate_range(max_heart_rate)

# Display the calculated target heart rate range.
display_target_heart_rate_range(lower_range, upper_range)



# #Prompt user to enter age

# user_age = int(input('Enter your age: '))

# # Calculate the maximum heart rate per minute.

# max_heartrate = 220 - user_age

# # Calculate the lower and upper bounds for the target heart rate range.
# lower_range = 0.65 * max_heartrate
# upper_range = 0.85 * max_heartrate

# # Display the calculated target heart rate range.
# print("To strengthen your heart, keep your heart rate between", lower_range, "and", upper_range, "for at least 20 minutes during exercise.")




