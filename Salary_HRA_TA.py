# Accept salary from user and add 10% of HRA on salary, 5% of TA on salary.

basic_salary = float(input("Enter Salary: "))
hra = (10 * basic_salary) / 100
ta = (5 * basic_salary) / 100
total_salary = basic_salary + hra + ta
print("The total salary is", total_salary)