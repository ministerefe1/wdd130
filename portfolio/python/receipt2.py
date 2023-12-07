# import csv
# from datetime import datetime


# def read_dictionary(product, key_column_index):
#     product_dict = {}
#     with open(product, "rt") as csvfile:
#         reader = csv.reader(csvfile)

#         for row_list in reader:
#             key = row_list[key_column_index]
#             value = row_list[1:]  # Include all columns except the first (Product #)
#             product_dict[key] = value

#     return product_dict


# def add_Item(request, product_data, quantity):
#     with open(request, mode="a", newline="") as request_csv:
#         writer = csv.writer(request_csv)
#         writer.writerow([product_data, quantity])


# # def generate_receipt(request_file, product_dict):
# #     try:
# #         # Get the current date and time
# #         current_date_and_time = datetime.now()

# #         # Print the store name at the top of the receipt
# #         print("Inkom Emporium")
# #         print(f"Receipt Date and Time: {current_date_and_time:%a %b %d %H:%M:%S %Y}")
# #         print("\nOrdered Items:")

# #         subtotal = 0
# #         total_items = 0

# #         # Open and process the request.csv file
# #         with open(request_file, "r") as request_file:
# #             reader = csv.reader(request_file)
# #             next(reader)  # Skip the header row

# #             for row in reader:
# #                 requested_product_number, requested_quantity = row

# #                 # Look up product details from product_dict
# #                 if requested_product_number in product_dict:
# #                     product_data = product_dict[requested_product_number]
# #                     product_name = product_data[0]

# #                     # Check the length before accessing index 1
# #                     product_price = product_data[1] if len(product_data) > 1 else "N/A"

# #                     item_total = float(product_price) * float(requested_quantity)
# #                     subtotal += item_total
# #                     total_items += int(requested_quantity)

# #                     # Print information for the ordered product
# #                     print(f"{product_name}: {requested_quantity} @ {product_price}")

# #                 else:
# #                     raise KeyError(
# #                         f"Unknown product ID in the request.csv file: {requested_product_number}"
# #                     )

# #         # Calculate sales tax (using 6% as the sales tax rate)
# #         sales_tax_rate = 0.06
# #         sales_tax_amount = subtotal * sales_tax_rate

# #         # Calculate total amount due
# #         total_due = subtotal + sales_tax_amount

# #         # Print additional details on the receipt
# #         print("\nSummary:")
# #         print(f"Number of Ordered Items: {total_items}")
# #         print(f"Subtotal: ${subtotal:.2f}")
# #         print(f"Sales Tax: ${sales_tax_amount:.2f}")
# #         print(f"Total: ${total_due:.2f}")

# #         # Print a thank you message
# #         print("\nThank you for shopping at the Inkom Emporium.")

# #         # Add features to exceed requirements
# #         if current_date_and_time.weekday() in {1, 2}:  # Tuesday or Wednesday
# #             print("Discount Applied: 10% off for Tuesday or Wednesday!")

# #         if current_date_and_time.hour < 11:  # Before 11:00 a.m.
# #             print("Discount Applied: 10% off for orders before 11:00 a.m!")

# #         # Print a coupon for one of the products ordered
# #         if total_items > 0:
# #             print("\nCoupon:")
# #             print(f"Get 20% off your next purchase of {product_name}!")

# #         # Print an invitation for an online survey
# #         print("\nSurvey Invitation:")
# #         print(
# #             "We value your feedback! Take our online survey for a chance to win a prize."
# #         )

# #     except FileNotFoundError:
# #         print("Error: Missing file. Please check the file path.")
# #     except KeyError as e:
# #         print(f"Error: {e}")
# #     except Exception as e:
# #         print(f"An unexpected error occurred: {e}")


# # if __name__ == "__main__":
# #     try:
# #         # Specify the file paths
# #         product_file_path = "products.csv"
# #         request_file_path = "request.csv"

# #         # Call the read_dictionary function to create a product dictionary
# #         products_dict = read_dictionary(product_file_path, key_column_index=0)

# #         # Call the add_Item function to add a new item to the request file
# #         add_Item(request_file_path, new_product_data="R002", new_quantity="3")

# #         # Generate and print the receipt
# #         generate_receipt(request_file_path, products_dict)


# #     except Exception as e:
# #         print(f"An unexpected error occurred: {e}")
# def generate_receipt(request_file, product_dict):
#     try:
#         # Get the current date and time
#         current_date_and_time = datetime.now()

#         # Print the store name at the top of the receipt
#         print("Inkom Emporium")
#         print(f"Receipt Date and Time: {current_date_and_time:%a %b %d %H:%M:%S %Y}")
#         print("\nOrdered Items:")

#         subtotal = 0
#         total_items = 0

#         # Check if it's Tuesday or Wednesday and apply a 10% discount
#         discount_percent = 0
#         if current_date_and_time.weekday() in {1, 2}:  # Tuesday or Wednesday
#             discount_percent = 0.10

#         # Check if it's before 11:00 a.m. and apply a 10% discount
#         if current_date_and_time.hour < 11:  # Before 11:00 a.m.
#             discount_percent = 0.10

#         # Open and process the request.csv file
#         with open(request_file, "r") as request_file:
#             reader = csv.reader(request_file)
#             next(reader)  # Skip the header row

#             for row in reader:
#                 requested_product_number, requested_quantity = row

#                 # Look up product details from product_dict
#                 if requested_product_number in product_dict:
#                     product_data = product_dict[requested_product_number]
#                     product_name = product_data[0]

#                     # Check the length before accessing index 1
#                     product_price = product_data[1] if len(product_data) > 1 else "N/A"

#                     # Apply discount if applicable
#                     discounted_price = float(product_price) - (
#                         float(product_price) * discount_percent
#                     )
#                     item_total = discounted_price * float(requested_quantity)

#                     subtotal += item_total
#                     total_items += int(requested_quantity)

#                     # Print information for the ordered product
#                     print(
#                         f"{product_name}: {requested_quantity} @ {product_price} (Discounted: {discount_percent * 100}%)"
#                     )

#                 else:
#                     raise KeyError(
#                         f"Unknown product ID in the request.csv file: {requested_product_number}"
#                     )

#         # Calculate sales tax (using 6% as the sales tax rate)
#         sales_tax_rate = 0.06
#         sales_tax_amount = subtotal * sales_tax_rate

#         # Calculate total amount due
#         total_due = subtotal + sales_tax_amount

#         # Print additional details on the receipt
#         print("\nSummary:")
#         print(f"Number of Ordered Items: {total_items}")
#         print(f"Subtotal: ${subtotal:.2f}")
#         print(f"Sales Tax: ${sales_tax_amount:.2f}")
#         print(f"Total: ${total_due:.2f}")

#         # Print a thank you message
#         print("\nThank you for shopping at the Inkom Emporium.")

#         # Print a coupon for one of the products ordered
#         if total_items > 0:
#             print("\nCoupon:")
#             print(f"Get 20% off your next purchase of {product_name}!")

#         # Print an invitation for an online survey
#         print("\nSurvey Invitation:")
#         print(
#             "We value your feedback! Take our online survey for a chance to win a prize."
#         )

#     except FileNotFoundError:
#         print("Error: Missing file. Please check the file path.")
#     except KeyError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# if __name__ == "__main__":
#     main()
print()

import csv
from datetime import datetime


def read_dictionary(product, key_column_index):
    product_dict = {}
    with open(product, "rt") as csvfile:
        reader = csv.reader(csvfile)

        for row_list in reader:
            key = row_list[key_column_index]
            value = row_list[1:]  # Include all columns except the first (Product #)
            product_dict[key] = value

    return product_dict


# def add_Item(request, product_data, quantity):
#     with open(request, mode="a", newline="") as request_csv:
#         writer = csv.writer(request_csv)
#         writer.writerow([product_data, quantity])


def generate_receipt(request_file, product_dict):
    try:
        # Get the current date and time
        current_date_and_time = datetime.now()

        # Print the store name at the top of the receipt
        print("Inkom Emporium")
        print(f"Receipt Date and Time: {current_date_and_time:%a %b %d %H:%M:%S %Y}")
        print("\nOrdered Items:")

        subtotal = 0
        total_items = 0

        # Check if it's Tuesday or Wednesday and apply a 10% discount
        discount_percent = 0
        if current_date_and_time.weekday() in {1, 2}:  # Tuesday or Wednesday
            discount_percent = 0.10

        # Check if it's before 11:00 a.m. and apply a 10% discount
        if current_date_and_time.hour < 11:  # Before 11:00 a.m.
            discount_percent = 0.10

        # Open and process the request.csv file
        with open(request_file, "r") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip the header row

            for row in reader:
                requested_product_number, requested_quantity = row

                # Look up product details from product_dict
                if requested_product_number in product_dict:
                    product_data = product_dict[requested_product_number]
                    product_name = product_data[0]

                    # Check the length before accessing index 1
                    product_price = product_data[1] if len(product_data) > 1 else "N/A"

                    # Apply discount if applicable
                    discounted_price = float(product_price) - (
                        float(product_price) * discount_percent
                    )
                    item_total = discounted_price * float(requested_quantity)

                    subtotal += item_total
                    total_items += int(requested_quantity)

                    # Print information for the ordered product
                    print(
                        f"{product_name}: {requested_quantity} @ {product_price} (Discounted: {discount_percent * 100}%)"
                    )

                else:
                    raise KeyError(
                        f"Unknown product ID in the request.csv file: {requested_product_number}"
                    )

        # Calculate sales tax (using 6% as the sales tax rate)
        sales_tax_rate = 0.06
        sales_tax_amount = subtotal * sales_tax_rate

        # Calculate total amount due
        total_due = subtotal + sales_tax_amount

        # Print additional details on the receipt
        print("\nSummary:")
        print(f"Number of Ordered Items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax_amount:.2f}")
        print(f"Total: ${total_due:.2f}")

        # Print a thank you message
        print("\nThank you for shopping at the Inkom Emporium.")

        # Print a coupon for one of the products ordered
        if total_items > 0:
            print("\nCoupon:")
            print(f"Get 20% off your next purchase of {product_name}!")

        # Print an invitation for an online survey
        print("\nSurvey Invitation:")
        print(
            "We value your feedback! Take our online survey for a chance to win a prize."
        )

    except FileNotFoundError:
        print("Error: Missing file. Please check the file path.")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Specify the file paths
    product_file_path = "products.csv"
    request_file_path = "request.csv"

    # Call the read_dictionary function to create a product dictionary
    products_dict = read_dictionary(product_file_path, key_column_index=0)

    # Call the add_Item function to add a new item to the request file
    # add_Item(request_file_path, new_product_data="R002", new_quantity="3")

    # Generate and print the receipt
    generate_receipt(request_file_path, products_dict)


if __name__ == "__main__":
    main()
