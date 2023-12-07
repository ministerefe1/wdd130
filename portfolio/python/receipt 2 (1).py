import csv
from datetime import datetime

def read_dictationary(filename, key_column_index):
    dictionary = {}
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row_list in reader:
            if len(row_list) > key_column_index:
                key = row_list[key_column_index]
                dictionary[key] = [row_list[1], row_list[2]]
                
    return dictionary

def main():
    try:
        products_dict = read_dictationary('products.csv', 0)
        print('Products Dictionary:')
        print(products_dict)
        print('\n')

        with open('request.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            store_name = 'Home Import'
            print(f'\n{store_name}\n')

            total_items = 0
            subtotal = 0

            print('Requested Items:')
            for row in reader:
                key = row[0]

                if key in products_dict:
                    product_info = products_dict[key]
                    product_name = product_info[0]
                    product_price = float(product_info[1])
                    requested_quantity = int(row[1])

                    print(f'{product_name}: {requested_quantity} @ {product_price:.2f}')
                    
                    total_items += requested_quantity
                    subtotal += requested_quantity * product_price
                else:
                    print(f'Product with key {key} not found in products_dict.\n')
       
            tax_rate = 0.06
            tax = subtotal * tax_rate
            total_due = subtotal + tax
            print(f'\n\nNumber of Items: {total_items}')
            print(f'Subtotal: {subtotal:.2f}')
            print(f'Sales Tax: {tax:.2f}')
            print(f'Total: {total_due:.2f}')

            print(f'\nThank you for shopping with us at {store_name}!!')

            current_datetime = datetime.now()
            print(f'{current_datetime:%a %b %d %H:%M %Y}')

    except FileNotFoundError:
        print('Error: File not found. Please check the file paths.')
    except KeyError:
        print('Error: KeyError occurred. Please check the structure of your CSV files.')

if __name__ == '__main__':
    main()
