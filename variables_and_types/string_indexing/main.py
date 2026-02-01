grocery_item = "Grilled Chicken Salad"

# 1. length
length_of_item = len(grocery_item)
 
# 2. first characters of each word
first_char = grocery_item[0]
second_char = grocery_item[8]
third_char = grocery_item[16]

# 3. last characters of each word (using negative indexes)
last_char1 = grocery_item[-1]
last_char2 = grocery_item[-7]
last_char3 = grocery_item[-15]

# Print statements (tests ignore output)
print("Length of item name:", length_of_item)
print("First characters:", first_char, second_char, third_char)
print("Last characters:", last_char1, last_char2, last_char3)