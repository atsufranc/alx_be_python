monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")


monthly_savings = int(monthly_income) - int(monthly_expenses)

#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))

projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#Your monthly savings are $.
print(f"Your monthly savings are ${monthly_savings}")
#Projected savings after one year, with interest
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
