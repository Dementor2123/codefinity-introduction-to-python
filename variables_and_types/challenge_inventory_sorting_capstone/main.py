# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]

category1 = categories[0:11]
category2 = categories[13:24]

bubblegam_price = "$1.50"
chokolate_price = "$2.00"
pasta_price = "$5.40"
print(
    "We have " + candy1 + " for " + bubblegam_price + " in the " + category1)
print("We have " + candy2 + " for " + chokolate_price + " in the " + category1)
print("We have " + dry_goods + " for" + pasta_price + " in the " + category2)
