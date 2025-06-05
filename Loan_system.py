house_value = float(input('Value of the house: $'))
salary = float(input("Buyer's salary: $"))
years = int(input('How many years of financing? '))

monthly_payment = house_value / (years * 12)
max_allowed_payment = salary * 30 / 100

print(f'To pay for a house of ${house_value:.2f} in {years} years, ', end='')
print(f'the monthly payment will be ${monthly_payment:.2f}')

if monthly_payment <= max_allowed_payment:
    print('Loan APPROVED!')
else:
    print('Loan DENIED!')