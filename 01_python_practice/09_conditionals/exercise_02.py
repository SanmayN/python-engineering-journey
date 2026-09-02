userScore = int(input("Enter the score for your Grade: "))

if 0 > userScore or userScore> 100:
    print("Invalid Score")
elif userScore >= 90:
    print("A")
elif userScore >= 80:
    print("B")
elif userScore >= 70:
    print("C")
elif userScore >= 60:
    print("D")
else:
    print("F")