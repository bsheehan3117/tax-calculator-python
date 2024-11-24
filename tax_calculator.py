'''
    CS5001
    Spring 2023
    HW1

    Brendan Sheehan
'''
'''
    This program takes the salary and investment income to determine the tax on the salary, capital gains tax, and total tax due.
'''

def main ():

    salary_income = float (input ("What is the salary income for the year?"))  #input annual salary
    investment_income = float (input ("What is the investment income for the year?"))  #input input annual investment income

    normal_income_tax = salary_income * .24  #calculate the amount of income tax
    capital_gains_tax = investment_income * .15  #calculate the amount of capital gains tax
    total_tax_due = normal_income_tax + capital_gains_tax  #calculate the total tax due

    print (f"Tax on your salary income is ${normal_income_tax:.2f}")  #print income tax
    print (f"Tax on your investment income is ${capital_gains_tax:.2f}")  #print capital gains tax
    print (f"Total tax is ${total_tax_due:.2f}")  #print total tax due

if __name__ == "__main__" :
    main ()
    
