balance = 999999
annualInterestRate = 0.18

def monthly_balance(i_bal, pay, rate_int_month):
    bal_pay = i_bal - pay
    f_bal = bal_pay + (rate_int_month * bal_pay)
    return f_bal

rate_int_month = annualInterestRate / 12
low = balance / 12
high = (balance*(1 + rate_int_month)**12) / 12
test_bal = balance

while test_bal > 0.01 or test_bal < 0:
    test_bal = balance
    pay = (low+high) / 2
    for i in range(12):
        test_bal = monthly_balance(test_bal, pay, rate_int_month)
    if test_bal > 0:
        low = pay
    else:
        high = pay

print('Lowest Payment:', round(pay, 2))
