#1.Create the Dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

#2.Check and Update Price
egg_price = grocery_inventory["Eggs"][1]
if egg_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    category, _, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, egg_price -1, stock)
else:
    print("The price of Eggs is reasonable.")

#3.Add a New Item
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

#Manage Stock
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    category, price, _ = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, milk_stock + 20)
else:
    print("Milk has sufficient stock.")

#5.Remove Item Based on Price
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.remove("Apples")
    print("Apples removed from inventory due to high price.")

#6.Final Print
print(f"Updated inventory: {grocery_inventory}")



