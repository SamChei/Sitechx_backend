loan = float(input("Enter the loan amount: "))
interest = float(input("Enter the interest rate (as a decimal): "))
repayment =float(input("Enter the repayment amount: "))
total_amount = loan + (loan * interest)

if repayment < total_amount:
    print("The repayment amount is less than the total amount due.")



print ("Interest charge is: ", interest)
print("Total amount is: ", total_amount)
