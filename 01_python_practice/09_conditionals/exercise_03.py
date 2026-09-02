userInput = input("Enter the month: ").upper()
season = ""
if (userInput == "SEPTEMBER" or userInput == "OCTOBER" or userInput == "NOVEMBER"):
    season = "Autumn"
elif (userInput == "DECEMBER" or userInput == "JANUARY" or userInput == "FEBRUARY"):
    season = "Winter"
elif (userInput == "MARCH" or userInput == "APRIL" or userInput == "MAY"):
    season = "Spring"
else:
    season = "Summer"

print(season)