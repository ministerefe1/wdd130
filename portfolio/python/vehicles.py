# def main():
#     # Create a dictionary that contains data about six vehicles.
#     # The key for each vehicle in the dictionary is the vehicle's
#     # identification number (VIN). The value for each vehicle is
#     # a list that contains the year, manufacturer, model, color,
#     # engine design, and engine displacement.
#     vehicles_dict = {
#         # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
#         "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
#         "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
#         "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
#         "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
#         "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
#         "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5],
#     }

#     MANUFACTURER_INDEX = 1
#     MODEL_INDEX = 2
#     COLOR_INDEX = 3

#     # Ask the user for a vehicle identification number (VIN).
#     vin = input("Please enter a VIN: ")

#     # Check if the vin is a key that is in the vehicles dictionary.
#     if vin in vehicles_dict:
#         print(f"vin is a key: {vin}")

#         # Find the data for the vehicle that the user wants.
#         pass

#         # Print the manufacturer, model, and color of the vehicle.
#         # Don't print the year, engine design, or displacement.
#         pass

#     else:
#         # Print a message stating that the VIN entered
#         # by the user is not in the dictionary.
#         print(f"{vin} is not in the dictionary.")


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
# if __name__ == "__main__":
#     main()
# print()


# def main():
#     number_list = ["6537", "2437", "1543", "7635", "4335"]
#     name_list = ["Othuke", "Obaro", "Zino", "Franca"]

#     students_dict = dict(zip(number_list, name_list))
#     print(students_dict)

#     # add from item
#     students_dict["7635"] = "Gladys"
#     print(students_dict)

#     # Remove item in dict

#     students_dict.pop("6537")
#     print(students_dict)

#     # Get the number of items in student_dict
#     lenght = len(students_dict)
#     print(lenght)

#     print(students_dict)

#     # get a student ID
#     id = input("Enter a student ID: ")

#     if id in students_dict:
#         name = students_dict[id]
#         print(name)

#     else:
#         print("There is no such student")


# if __name__ == "__main__":
#     main()

# print()


def main():
    students_dict = {
        # student_ID: [given_name, surname, email_address, credits]
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Amelia", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Ana", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Amelia", "Davis" "dav19008@byui.edu", 0],
    }

    Given_Name_Index = [0]
    Surname_Index = [1]
    Email_Index = [2]
    Credit_Index = [3]

    id = input("Enter student ID: ")
    if id in students_dict:
        # Find the student ID in the dictionary and
        # retrieve the corresponding value, which is a list.
        value = students_dict[id]

        # Retrieve the student's given name (first name) and
        # surname (last name or family name) from the list.
        given_name = value[0]
        surname = value[1]

        print(f"{given_name} {surname}")

    else:
        print("No such student")


if __name__ == "__main__":
    main()
