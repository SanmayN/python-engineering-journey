userinput = int(input("Enter your age:"))
underage = 18 - userinput
if userinput >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {underage} more years to learn to drive.")