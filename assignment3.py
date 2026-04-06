cafe_info = ("Brew & Bite", "Astana, Mangilik El 1", "Good food,great vibes")
print("="*30)
print(cafe_info[0])
print(cafe_info[1])
print(cafe_info[2])
print("="*30)

items = []
prices = []

while True:
    name = input("Enter item name (or 'done' to finish)")
    if name == "done":
        break
    items.append(name)
    prices.append(float(input("Enter price of item: ")))

print("-"*30)
print(f'Your order ({len(items)} items): ')
print("-"*30)
for i in range(0,len(items)):
    print(f"{items[i]} {prices[i]} KZT")
print("-"*30)

uniq_drinks = set()
while True:
    drink_name = input("Enter drink name (or 'done' to finish): ")
    if drink_name == "done":
        break
    uniq_drinks.add(drink_name)
print("uniq drinks today:", len(uniq_drinks))
print(uniq_drinks)

price_total = sum(prices)
f=True
price_total_dis=0
name = input("Enter customer name: ")
hour = int(input("Enter current hour (0-23): "))
print("="*30)
print("BILL - Brew & Bite")
print("="*30)
print("Customer :", name)
print("Items :", len(items))
print("-"*30)
for i in range(0,len(items)):
    print(f"{items[i]} {prices[i]} KZT")
print("-"*30)
print("Subtotal :", price_total)
if 6<= hour < 12:
    price_total_dis = price_total * 0.1
    print("Morning Discount 10% : ", price_total_dis)
elif 12 <= hour < 17:
    print("No Discount")
elif 17 <= hour < 22:
    price_total_dis = price_total * 0.05
    print("Evening Discount 5% : ", price_total_dis)
else:
    print("Closed")
    f= False
total_after_dis = (price_total - price_total_dis)
if f:
    print("Tip (10%): ", total_after_dis * 0.1)
    print("Total : ", total_after_dis + total_after_dis * 0.1)
print('='*30)
