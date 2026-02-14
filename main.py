# Monthly savings calculator

monthly_income = 3500
monthly_expenses = 2200

monthly_savings = monthly_income - monthly_expenses

print("Monthly Income:", monthly_income)
print("Monthly Expenses:", monthly_expenses)
print("Monthly Savings:", monthly_savings)
annual_interest_rate = 0.05  # 5%
years = 5
months = years * 12
monthly_rate = annual_interest_rate / 12

total_savings = 0

for month in range(1, months + 1):
    total_savings = (total_savings + monthly_savings) * (1 + monthly_rate)

    if month % 12 == 0:
        print("Year", month // 12, "Total Savings:", round(total_savings, 2))
