#A user is considered to have achieved the daily fitness goal when the number of steps is greater than 10000 or 
# the number of active minutes is greater than 30.

steps = int(input())
active_minutes = int(input())

goal_achieved = (steps > 10000) or (active_minutes > 30)

print(goal_achieved)

