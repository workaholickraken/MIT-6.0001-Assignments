
annual_salary = int(input("Enter your starting annual salary: "))
semi_annual_raise=.07
total_cost = 1000000
down_payment = 0.25 * total_cost
current_savings = 0.0
r = 0.04
months = 0
step=0
low=0
high=10000
portion_saved= (high+low)/2
portion_saved_rate= portion_saved/ float(10000)
monthly_salary = annual_salary / 12
monthly_savings = portion_saved_rate * monthly_salary

if (monthly_salary*36)< down_payment:
  print("It is not possible to save for a down payment in 36 months.")
  i=False

else :
  i=True
  while i:  
    while abs(current_savings- down_payment) >=100 :
        ROI = current_savings * r / 12
        current_savings += ROI + monthly_savings
        if months % 6==0 and months<37:
          monthly_salary+=monthly_salary*semi_annual_raise
          monthly_savings=portion_saved_rate*monthly_salary
        months += 1  
        if months==36:
          break
      
          
    if  current_savings- down_payment >100 :
          high=portion_saved
          portion_saved= (high+low)/2 
          portion_saved_rate= portion_saved/ float(10000)
    elif down_payment-current_savings >100:
          low=portion_saved
          portion_saved= (high+low)/2 
          portion_saved_rate= portion_saved/ float(10000)
    else:
          print("Best savings rate:", portion_saved_rate)
          print("Steps in bisection search:",step)
          i=False

    step+=1
    current_savings=0
    ROI=0
    months=0
    monthly_salary = annual_salary / 12
    monthly_savings = portion_saved_rate * monthly_salary
