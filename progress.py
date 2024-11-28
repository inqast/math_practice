import datetime as dt

hoursTotal = 50 + 20 + 50 + 30 + 33 + 57 + 33


start = dt.datetime(2024, 3, 11)
end = dt.datetime(2024, 9, 11)
today = dt.datetime.now()

weeksTotal = (end - start).days // 7
currentWeek = (today - start).days // 7

hoursAWeek = hoursTotal//weeksTotal
hoursShouldBeDone = hoursAWeek*currentWeek

print("total weeks:", weeksTotal)
print("hours in a week:", hoursAWeek)
print("currentWeek:", currentWeek)
print("hoursShoulBeDone", hoursShouldBeDone)