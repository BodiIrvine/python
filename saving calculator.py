#here is where you input the goal for the year
goal = float(input('how much do you need to save this year'))

#here is where the calculations are taking place
monthly_goal = round(goal / 12, 2)
weekly_goal = round(goal / 52, 2)
daily_goal = round(goal / 365, 2)

#here is where all the printing takes place
print("to reach your goal of $" + str(goal) + " you will need to save")
print("$" + str(monthly_goal) + " per month")
print("$" + str(weekly_goal) + "per week")
print("$" + str(daily_goal) +  " per day")
