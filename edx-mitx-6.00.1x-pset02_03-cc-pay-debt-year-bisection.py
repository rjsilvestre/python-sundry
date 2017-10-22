# Program that calculates the minimum fixed monthly payment 
# needed in order pay off a credit card balance within 12 months. 
# A fixed monthly payment is a single number which does not 
# change each month, but instead is a constant amount that 
# will be paid each month.
# This version uses bisection search to find the minimum payment.
# As a result the program runs faster and the result is precise.


# Test case
balance = 999999
annualInterestRate = 0.18

def monthly_balance(i_bal, pay, rate_int_month):
    '''
    Calculates the monthly balance of a credit card.

    Args:
        i_bal: Initial balance.
        pay: Payment amount.
        rate_int_month: Monthly interest rate.
    
    Returns:
        The final balance of the month.
    '''
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
