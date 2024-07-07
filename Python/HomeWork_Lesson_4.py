# HomeWork_Lesson_4
# ANSWER_1

def generate_receipt(item1_name, item1_price, item2_name, item2_price, item3_name, item3_price):
    # Calculate the total price
    total_price = item1_price + item2_price + item3_price

    # Print the detailed receipt
    print(f"{item1_name.ljust(15)} {item1_price:.2f}")
    print(f"{item2_name.ljust(15)} {item2_price:.2f}")
    print(f"{item3_name.ljust(15)} {item3_price:.2f}")
    print("-" * 20)
    print(f"TOTAL{''.ljust(10)} {total_price:.2f}")


# Example usage:
Item_1_name = 'Trainers'
Item_1_price = 50.45
Item_2_name = 'T-shirt'
Item_2_price = 12.00
Item_3_name = 'Jeans'
Item_3_price = 35.75
generate_receipt(Item_1_name, Item_1_price, Item_2_name, Item_2_price, Item_3_name, Item_3_price)
