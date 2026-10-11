# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

month = input("Enter Month: ").upper()
def check_season(month):
    if month in ("JANUARY", "FEBRUARY", "DECEMBER"): #membership check
        return "Winter"
    elif month in ("MARCH","APRIL","MAY"):
        return "Spring"
    elif month == "JUNE" or month == "JULY" or month == "AUGUST": # Normal repititive pattern
        return "Summer"
    elif month == "SEPTEMBER" or month == "OCTOBER" or month == "NOVEMBER":
        return "Autumn"

print(check_season(month))