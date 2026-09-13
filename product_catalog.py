from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.

# print(products)

# for product in products:
#     print(product["name"])


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []
response = ""

while response != "N":
    print("Input a preference:")
    preference = input().lower()

    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()


# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.

converted_products = products

for index in range(len(converted_products)):
    converted_products[index]["tags"] = set(converted_products[index]["tags"])


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''

    counter = 0

    for product_tag in product_tags:
        for customer_tag in customer_tags:
            if product_tag == customer_tag:
                counter += 1

    return counter


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''

    recommendation_list = []
    num = 0

    for product in products:
        num = count_matches(product["tags"], customer_tags)

        if num != 0:
            recommendation_list.append([product["name"], num])

    recommendation_list = sorted(recommendation_list, key=lambda list: list[1])

    return recommendation_list


# TODO: Step 7 - Call your function and print the results

customer_recommendations = recommend_products(converted_products, customer_preferences)

print("------------------------")
print("Recommended Products:")
print("------------------------")

if len(customer_recommendations) == 0:
    print("No matches found.")
else:
    for product in customer_recommendations[::-1]:  #loop through list starting at the last element
        print("-", product[0], "(" +str(product[1]), "match(es))")
        

# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
""" 
The core operations I used throughout the program were loops and conditional statements. 
I determined which operations to use based on what task I needed to accomplish. 
For instance, I used for loops when I needed to loop a specific amount of times, such as when iterating through the items in a list or set. 
On the other hand, the while loop was used when the total number of required iterations was unknown, like when gathering customer input. 
Conditional statements were used when I needed to control the direction of the program. 
For example, I used if statements to count the number of matches, add products to the recommendation list, and handle cases where there were no matches found.  
"""
# 2. How might this code change if you had 1000+ products?
"""
If there were a very large number of products, this code would need to be written with more efficiency in mind. 
Converting the lists into sets was one way to make the code more efficient. 
Additionally, with 1000+ products, the chance of there being duplicates in the data increases. 
Converting the lists into sets ensures there won’t be any repeated products or tags to slow down execution. 
Using classes could also make the code more organized and easier to modify in the future. 
"""
