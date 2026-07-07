def calculate_balance(loan_amount, interest_rate):
    interest = loan_amount * (interest_rate / 100)
    return loan_amount + interest


def repay(balance):
    repayment = float(input("Enter repayment amount: "))
    balance -= repayment

    if balance > 0:
        print(f"Remaining Loan Balance: {balance}")
    elif balance == 0:
        print("Loan fully repaid!")
    

    elif repayment > balance:
        extra = repayment - balance
        print(f"You overpaid by {extra}")
        balance = 0
    else:
        balance = balance - repayment

    print(f"Remaining Loan Balance: {balance}")


def main():
    loan = float(input("Enter loan amount: "))
    rate = float(input("Enter interest rate (%): "))

    balance = calculate_balance(loan, rate)
    print("Total Loan Balance:", balance)

    repay(balance)


main()