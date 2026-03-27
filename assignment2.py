name = input("Enter customer name: ")
item_c = 0
price_total = 0
while True:
    item_name = input("Enter name of item (or 'done' to finish): ")
    if item_name == "done": break
    price = float(input("Enter price of item: "))
    item_c+=1
    price_total += price

print("Customer :", name.upper())
print("Items :", item_c)
print("Subtotal :", price_total, "KZT")

hour = int(input("Enter current hour (0-23): "))
price_total_dis = 0
f = True
print('-'*30)
if 6<= hour < 12:
    print("Morning Discount")
    price_total_dis = price_total * 0.1
elif 12 <= hour < 17:
    print("No Discount")
elif 17 <= hour < 22:
    print("Evening Discount")
    price_total_dis = price_total * 0.05
else:
    print("Closed")
    f= False
total_after_dis = (price_total - price_total_dis)
if f:
    print("Discount : ", price_total_dis)
    print("Tip : ", total_after_dis * 0.1)
    print("Total : ", total_after_dis + total_after_dis * 0.1)
print('-'*30)

print("Name uppercase : ", name.upper())
print("Name lowercase : ", name.lower())
print("Name length : ", len(name))

if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")