goal = float(input('how much do you need to save this year'))


monthly_goal = round(goal / 12, 2)

weekly_goal = round(goal / 52, 2)

daily_goal = round(goal / 365, 2)

print("you will need to save $" + str(monthly_goal) + " per month, $" + str(weekly_goal) + " every week, $" + str(daily_goal) +  " per day to achieve your goal of saving $" + str(goal) + " over the next year!")
