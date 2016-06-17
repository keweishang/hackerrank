# Separate a string by sep from the rear 
name,space,price = raw_input().rpartition(' ')

# Iterate through dict items, each item is a tuple
for item_name, net_price in my_order.items():
    print item_name, net_price

# Create a list of list using for loop
b = [[1,2,3,4,5,6,7] for _ in range(n)]