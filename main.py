# Day 2 - Control & Logic

monthly_savings = 1300
annual_interest_rate = 0.05
monthly_rate = annual_interest_rate / 12

months = 300
month = 1
total = 0

while month <= months:
    total = (total + monthly_savings) * (1 + monthly_rate)

    if total >= 100000:
        print("You have reached your goal in", month, "months!")
        break

    if month % 12 == 0:
        print("Year", [month // 12], "Total", round(total, 2))

    month = month + 1

   



