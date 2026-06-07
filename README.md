item1 = 100
item2 = 200
item3 = 300
budget = 500
total_price = item1 + item2 + item3
print (total_price)
if total_price <= budget:
    print ("you can buy all items")
if total_price > budget:
    print ("you cannot buy all items")
    difference = total_price - budget
    print (difference)
