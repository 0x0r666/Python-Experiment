
#Aim: Write a Program to implement control flow statements and looping statements in python.

# -------- PLAYER DATA --------
runs = int(input("Enter runs scored: "))
balls = int(input("Enter balls faced: "))
wickets = int(input("Enter wickets taken: "))
runs_conceded = int(input("Enter runs conceded: "))
overs = float(input("Enter overs bowled: "))
catches = int(input("Enter catches taken: "))

# Calculations
strike_rate = (runs / balls) * 100
economy = runs_conceded / overs

# Batting Performance (if–elif–else)
if runs >= 50 and strike_rate >= 120:
    batter = "Excellent"
elif runs >= 30 and strike_rate >= 100:
    batter = "Good"
elif runs >= 20:
    batter = "Average"
else:
    batter = "Poor"

# Bowling Performance (if–elif–else)
if wickets >= 3 and economy <= 6:
    bowler = "Excellent"
elif wickets >= 2 and economy <= 8:
    bowler = "Good"
elif wickets >= 1:
    bowler = "Average"
else:
    bowler = "Poor"

# Fielding Performance (if–elif–else)
if catches >= 2:
    fielder = "Outstanding"
elif catches == 1:
    fielder = "Active"
else:
    fielder = "Needs Improvement"

# All-rounder
if batter=="Excellent" and bowler == "Excellent":
    overall = "Star All rounder"
elif batter=="Good" and bowler =="Good":
    overall = "Strong All rounder"
else:
    overall = "Needs Improvement"

print("Strike Rate:", strike_rate)
print("Economy:", economy)
print("Batting:", batter)
print("Bowling:", bowler)
print("Fielding:", fielder)
print("Overall:", overall)
