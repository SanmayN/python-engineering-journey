fruits = ['banana', 'orange', 'mango', 'lemon']

userInput = input("Please enter your favorite fruit: ").lower()
if userInput in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(userInput)
    print(fruits)