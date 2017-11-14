# This program calculate the credit card balance after one year 
# if a person only pays the minimum monthly payment required by 
# the credit card company each month.


# Test case
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def monthly_balance(i_bal, rate_pay, rate_int_month):
    '''
    Calculates the monthly balance of a credit card.

    Args:
        i_bal: Initial balance.
        rate_pay: Rate of the payment.
        rate_int_month: Monthly interest rate.
    
    Returns:
        The final balance of the month.
    '''
    pay = i_bal * rate_pay
    bal_pay = i_bal - pay
    f_bal = bal_pay + (rate_int_month * bal_pay)
    return round(f_bal, 2)

rate_int_month = annualInterestRate / 12

for i in range(12):
    balance = monthly_balance(balance, monthlyPaymentRate, rate_int_month)

print('Remaining balance:', balance)
