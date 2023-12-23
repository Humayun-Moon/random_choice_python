import random
option = ['book', 'pen', 'phone']
user = None 

user = input("Enter your choice to buy : ")
computer = random.choice(option)

print(f"Your Choice: {user}")
print(f"coumputer Choice: {computer}")

if user == computer:
    print("You won")
else:
    print('You lost')    