#Project 1 - Income Tax Calculator
#COP1047
#Michael Perez
#10/21/2022
#######main
tax_rate = 0.20
standard_deduction = 10000
dependent_deduction = 3000
#body
gross = float(input('Enter the gross income: '))
dependent = int(input('Enter the number of dependents: '))
total = gross - standard_deduction - (dependent_deduction * dependent)
income_tax = total * tax_rate
#end
print ('The income tax is $', income_tax)