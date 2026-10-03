name = input ("What's your name: ")
print (f"Welcome, {name}")
print("Welcome" + name)

item1 = input("First Expense: ")
amount = float(input("Amount: "))

print()
print("---------------------------SUMMARY-----------------------")
print(f" - {item1}: ${amount}")
print("---------------------------------------------------------")