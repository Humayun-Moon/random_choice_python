buyes = []
prices = []
total = 0

while True:
    buy = input("Enter What you like to purchase(Q to quit) :   ")
    if buy == "q":
        break
    else: 
        price = float(input("What amount of like buy :$     "))
        buyes.append(buy)
        prices.append(price)
       

print("----------------------------------")
print("---------Your Cart----------------")
print("----------------------------------")


print("You added to Cart: ")
for buy in buyes:
    print(buy, end=" ")
print()    