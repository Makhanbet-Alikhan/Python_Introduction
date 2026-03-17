name = input("Enter customer name: ")
item_name1 = input("Enter name of item 1: ")
price1 = float(input("Enter price of item 1 (KZT): "))
item_name2 = input("Enter name of item 2: ")
price2 = float(input("Enter price of item 2 (KZT): "))
people = int(input("Enter number of people: "))

subtotal = price1 + price2
tip = subtotal * 0.1
total = subtotal + tip
per_person = total / people

print("="*30)
print(" "*9,"CAFE BILL")
print("="*30)
print("Customer : ",name)
print(item_name1, " : ", price1, "KZT")
print(item_name2, " : ", price2, "KZT")
print("-"*30)
print("Subtotal : ", subtotal,  "KZT")
print("Tip (10%) : ", tip, "KZT")
print('Total : ',total, "KZT")
print("Per person : ",per_person,  "KZT")
print("="*30)

print("Tip included:", tip > 0)
print("Bill over 5000.0 KZT:", total>5000)