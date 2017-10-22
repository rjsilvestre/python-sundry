# Program that calculates the minimum fixed monthly payment 
# needed in order pay off a credit card balance within 12 months. 
# A fixed monthly payment is a single number which does not 
# change each month, but instead is a constant amount that 
# will be paid each month.


#Test case
balance = 3926
annualInterestRate = 0.2

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
