annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
current_savings = 0.0
r = 0.04
months = 0
down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
monthly_savings = portion_saved * monthly_salary

while current_savings < down_payment:
    ROI = current_savings * r / 12
    current_savings += ROI + monthly_savings
    months += 1

print(current_savings >= down_payment)
print("Number of months:", months)
