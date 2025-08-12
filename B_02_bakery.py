import pandas
import numpy


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_ans_list=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # check if the response is the entire world
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


def instructions():
    print(make_statement("Instructions", "📋"))
    print('''
Welcome to the Bakery Ordering Assistant!

You will:
- Enter your name
- Enter your budget between $3 & $50 ( as a whole integer )
- View a numbered menu of bakery items
- Enter the number of the item you want to buy
- Confirm it, and your budget updates
- Keep buying until you're finished or out of money
A final receipt will be shown at the end.
        ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.")


def int_check(question, low, high):
    """Checks users enter an integer between two values / float that is more than zero (or the 'xxx' exit code)"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == "xxx":
            return response

        try:
            # change the response to an integer and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine goes here

# Initialise ticket numbers
MAX_SPEND = 8

# lists to hold ticket details
all_menu = ["Croissant", "Bagel", "Muffin", "Donut", "Sourdough Loaf", "Cupcake"]
all_item_costs = [4.50, 5.50, 4.00, 3.50, 8.00, 3.00]

bakery_item_dict = {
    'Item Name': all_menu,
    'Ticket Price': all_item_costs,
}

# create dataframe / table from dictionary
bakery_frame = pandas.DataFrame(bakery_item_dict)

# Rearranging index
bakery_frame.index = numpy.arange(1, len(bakery_frame) + 1)

# Program main heading
print(make_statement("Bakery Ordering Assistant", "🍞"))

# Ask user if they want to see the instructions
# display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# Ask for their budget and check it's between 3 and 50
budget = int_check("Budget: ", 3, 50)

purchased_items = []
purchased_items_prices = []

# creating dictionary for receipt
purchased_dict = {
    'Item Name': purchased_items,
    'Item Prices': purchased_items_prices
}

# Loop to get name, age and budget details
while budget <= MAX_SPEND:

    print()

    # Display menu items
    print("This is the list of baked goods we have on offer :")
    print(bakery_frame)

    # Prompt the user to select a row using the index
    try:
        # ask for the user item
        choice = int_check("Enter the number of the item you would like to choose: ", 1, 6)

        selected_row = all_menu[choice - 1]
        item_price = all_item_costs[choice - 1]

        if budget >= item_price:
            budget -= item_price

            purchased_items.append(selected_row)
            purchased_items_prices.append(item_price)

            # display user selection
            print(f"You selected: {selected_row} ${item_price}")

            print(f"your new budget is: {budget} ")

        else:
            print("You cannot afford this card. Please choose a different one.")
            continue

        repurchase = string_check("Would you like to make another purchase? ")
        if repurchase == "no":
            break

        else:
            print("Invalid number. Please choose between 1-10.")
            continue

    except ValueError:
        print("Please enter a valid number.")
# End of Ticket Loop
