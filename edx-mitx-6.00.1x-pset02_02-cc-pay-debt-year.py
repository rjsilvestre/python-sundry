balance = 3926
annualInterestRate = 0.2

def monthly_balance(i_bal, pay, rate_int_month):
    bal_pay = i_bal - pay
    f_bal = bal_pay + (rate_int_month * bal_pay)
    return round(f_bal, 2)

rate_int_month = annualInterestRate / 12
pay = 0
test_bal = balance

while test_bal > 0:
    pay += 10
    test_bal = balance
    for i in range(12):
        test_bal = monthly_balance(test_bal, pay, rate_int_month)

print('Lowest Payment:', pay)
