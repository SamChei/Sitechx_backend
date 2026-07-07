loan_amount = float(input("Enter the loan amount: Ksh "))
interest_rate = float(input("Enter annual interest rate (%): "))

interest_charge = loan_amount * (interest_rate / 100)


total_balance = loan_amount + interest_charge

print("\n------ Loan Details ------")
print(f"Original Loan: Ksh {loan_amount:.2f}")
print(f"Interest Charge: Ksh {interest_charge:.2f}")
print(f"Total Loan Balance: Ksh {total_balance:.2f}")

repayment = float(input("\nEnter repayment amount: Ksh "))

remaining_balance = total_balance - repayment

if remaining_balance < 0:
    print("\nRepayment exceeds the loan balance.")
    print(f"Change to return: Ksh {-remaining_balance:.2f}")
    remaining_balance = 0

print(f"Remaining Loan Balance: Ksh {remaining_balance:.2f}")