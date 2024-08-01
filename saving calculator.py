goal = float(input('how much do you need to save this year'))


monthly_goal = round(goal / 12, 2)

weekly_goal = round(goal / 52, 2)

daily_goal = round(goal / 365, 2)

print("to reach your goal of $" + str(goal) + " you will need to save")
print("$" + str(monthly_goal) + " per month")
print("$" + str(weekly_goal) + "per week")
print("$" + str(daily_goal) +  " per day")
